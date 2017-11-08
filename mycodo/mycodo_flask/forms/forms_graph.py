# -*- coding: utf-8 -*-
#
# forms_graph.py - Graph Flask Forms
#

from flask_babel import lazy_gettext
from flask_wtf import FlaskForm

from wtforms import BooleanField
from wtforms import DecimalField
from wtforms import IntegerField
from wtforms import SelectMultipleField
from wtforms import SubmitField
from wtforms import StringField
from wtforms import validators
from wtforms import widgets

from wtforms.validators import DataRequired


class GraphAdd(FlaskForm):
    graph_type = StringField('Type', widget=widgets.HiddenInput())
    name = StringField(
        lazy_gettext(u'Name'),
        render_kw={"placeholder": lazy_gettext(u"Graph Name")},
        validators=[DataRequired()]
    )
    pid_ids = SelectMultipleField(lazy_gettext(u'PIDs'))
    relay_ids = SelectMultipleField(lazy_gettext(u'Outputs'))
    sensor_ids = SelectMultipleField(lazy_gettext(u'Inputs'))
    width = IntegerField(
        lazy_gettext(u'Width'),
        validators=[validators.NumberRange(
            min=1,
            max=12
        )]
    )
    height = IntegerField(
        lazy_gettext(u'Height (pixels)'),
        render_kw={"placeholder": lazy_gettext(u"Height (pixels)")},
        validators=[validators.NumberRange(
            min=100,
            max=10000
        )]
    )
    xaxis_duration = IntegerField(
        lazy_gettext(u'x-Axis (minutes)'),
        render_kw={"placeholder": lazy_gettext(u"X-Axis Duration")},
        validators=[validators.NumberRange(
            min=1,
            message=lazy_gettext(u"Number of minutes to display of past "
                                 u"measurements.")
        )]
    )
    refresh_duration = IntegerField(
        lazy_gettext(u'Refresh (seconds)'),
        render_kw={"placeholder": lazy_gettext(u"Refresh duration")},
        validators=[validators.NumberRange(
            min=1,
            message=lazy_gettext(u"Number of seconds to wait between acquiring"
                                 u" any new measurements.")
        )]
    )
    enable_navbar = BooleanField(lazy_gettext(u'Enable Navbar'))
    enable_export = BooleanField(lazy_gettext(u'Enable Export'))
    enable_range = BooleanField(lazy_gettext(u'Enable Range Selector'))
    Submit = SubmitField(lazy_gettext(u'Create'))


class GaugeAdd(FlaskForm):
    graph_type = StringField('Type', widget=widgets.HiddenInput())
    name = StringField(
        lazy_gettext(u'Name'),
        render_kw={"placeholder": lazy_gettext(u"Name")},
        validators=[DataRequired()]
    )
    sensor_ids = SelectMultipleField(lazy_gettext(u'Measurement'))
    width = IntegerField(
        lazy_gettext(u'Width'),
        validators=[validators.NumberRange(
            min=1,
            max=12
        )]
    )
    height = IntegerField(
        lazy_gettext(u'Height (pixels)'),
        render_kw={"placeholder": lazy_gettext(u"Height (pixels)")},
        validators=[validators.NumberRange(
            min=100,
            max=10000
        )]
    )
    y_axis_min = DecimalField(lazy_gettext(u'Gauge Min'))
    y_axis_max = DecimalField(lazy_gettext(u'Gauge Max'))
    max_measure_age = DecimalField(lazy_gettext(u'Max Age (seconds)'))
    refresh_duration = IntegerField(
        lazy_gettext(u'Refresh (seconds)'),
        render_kw={"placeholder": lazy_gettext(u"Refresh duration")},
        validators=[validators.NumberRange(
            min=1,
            message=lazy_gettext(u"Number of seconds to wait between acquiring"
                                 u" any new measurements.")
        )]
    )
    Submit = SubmitField(lazy_gettext(u'Create'))


class GraphMod(FlaskForm):
    graph_id = IntegerField('Graph ID', widget=widgets.HiddenInput())
    graph_type = StringField('Type', widget=widgets.HiddenInput())
    name = StringField(
        lazy_gettext(u'Name'),
        render_kw={"placeholder": lazy_gettext(u"Graph Name")},
        validators=[DataRequired()]
    )
    pid_ids = SelectMultipleField(lazy_gettext(u'PIDs'))
    relay_ids = SelectMultipleField(lazy_gettext(u'Outputs'))
    sensor_ids = SelectMultipleField(lazy_gettext(u'Inputs'))
    width = IntegerField(
        lazy_gettext(u'Width'),
        validators=[validators.NumberRange(
            min=1,
            max=12
        )]
    )
    height = IntegerField(
        lazy_gettext(u'Height (pixels)'),
        render_kw={"placeholder": lazy_gettext(u"Height (pixels)")},
        validators=[validators.NumberRange(
            min=100,
            max=10000
        )]
    )
    xaxis_duration = IntegerField(
        lazy_gettext(u'x-Axis (minutes)'),
        render_kw={"placeholder": lazy_gettext(u"X-Axis Duration")},
        validators=[validators.NumberRange(
            min=1,
            message=lazy_gettext(u"Number of minutes to display of past "
                                 u"measurements.")
        )]
    )
    refresh_duration = IntegerField(
        lazy_gettext(u'Refresh (seconds)'),
        render_kw={"placeholder": lazy_gettext(u"Refresh duration")},
        validators=[validators.NumberRange(
            min=1,
            message=lazy_gettext(u"Number of seconds to wait between acquiring"
                                 u" any new measurements.")
        )]
    )
    enable_navbar = BooleanField(lazy_gettext(u'Enable Navbar'))
    enable_export = BooleanField(lazy_gettext(u'Enable Export'))
    enable_range = BooleanField(lazy_gettext(u'Enable Range Selector'))
    use_custom_colors = BooleanField(lazy_gettext(u'Enable Custom Colors'))
    Submit = SubmitField(lazy_gettext(u'Save'))


class GaugeMod(FlaskForm):
    graph_id = IntegerField('Graph ID', widget=widgets.HiddenInput())
    graph_type = StringField('Type', widget=widgets.HiddenInput())
    name = StringField(lazy_gettext(u'Name'))
    sensor_ids = SelectMultipleField(lazy_gettext(u'Measurement'))
    width = IntegerField(lazy_gettext(u'Width'))
    height = IntegerField(lazy_gettext(u'Height (pixels)'))
    y_axis_min = DecimalField(lazy_gettext(u'Gauge Min'))
    y_axis_max = DecimalField(lazy_gettext(u'Gauge Max'))
    max_measure_age = DecimalField(lazy_gettext(u'Max Age (seconds)'))
    refresh_duration = IntegerField(lazy_gettext(u'Refresh (seconds)'))
    Submit = SubmitField(lazy_gettext(u'Save'))


class GraphDel(FlaskForm):
    graph_id = IntegerField('Graph ID', widget=widgets.HiddenInput())
    Submit = SubmitField(lazy_gettext(u'Delete'))


class GraphOrder(FlaskForm):
    orderGraph_id = IntegerField('Graph ID', widget=widgets.HiddenInput())
    orderGraphUp = SubmitField(lazy_gettext(u'Up'))
    orderGraphDown = SubmitField(lazy_gettext(u'Down'))
