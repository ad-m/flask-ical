import datetime
from calendar import HTMLCalendar
from datetime import date
from itertools import groupby
import requests
import requests_cache
import icalendar


class EventsCalendar(HTMLCalendar):
    def __init__(self, events, *args, **kwargs):
        super(EventsCalendar, self).__init__(*args, **kwargs)
        self.events = self.group_by_day(events)

    def formatday(self, day, weekday):
        if day != 0:
            cssclass = self.cssclasses[weekday]
            if date.today() == date(self.year, self.month, day):
                cssclass += ' today'
            if day in self.events:
                cssclass += ' filled'
                body = ['<ul>']
                for row in self.events[day]:
                    body.append(self.get_row_content(row))
                body.append('</ul>')
                return self.day_cell(cssclass, '%d %s' % (day, ''.join(body)))
            return self.day_cell(cssclass, day)
        return self.day_cell('noday', '&nbsp;')

    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super(EventsCalendar, self).formatmonth(year, month)

    def group_by_day(self, events):
        return {day: list(items) for day, items in groupby(events, lambda x: x[1]['DTSTART'].dt.day)}

    def day_cell(self, cssclass, body):
        return '<td class="%s">%s</td>' % (cssclass, body)

    def get_field(self):
        return self.field

    def get_row_content(self, row):
        return dict2table(dict(row[1]))


def dict2table(data):
    def _converter(data, key='Key', value='Value'):
        yield u'<table class="event">'
        yield u'<tr><th>{0}</th><th>{1}</th></tr>'.format(key, value)
        for key, value in data.items():
            if key == 'DTSTART':
                value = value.dt
            yield u'<tr><td>{0}</td><td>{1}</td></tr>'.format(key, value)
        yield u'</table>'
    return u"\n".join(_converter(data))


def calendar_range(components, year=date.today().month, month=date.today().year):
    return [(key, x) for key, x in components
        if x['DTSTART'].dt.month == month and
        x['DTSTART'].dt.year == year]


def calendar_sort(components):
    def key(obj):
        if isinstance(obj, datetime.datetime):
            return obj.date
        return obj
    components.sort(key=key)
    return components


def url2ical(url):
    req = requests.get(url)
    return icalendar.Calendar.from_ical(req.text)


def url2html(url, year=None, month=None):
    cal = url2ical(url)
    components = list(enumerate(cal.subcomponents))
    components = calendar_sort(components)
    components = calendar_range(components, year, month)
    return EventsCalendar(components).formatmonth(year, month)
