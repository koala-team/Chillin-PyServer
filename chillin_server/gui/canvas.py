# -*- coding: utf-8 -*-

# project imports
from ..config import Config
from .parser import Parser
from .messages import CanvasAction
from .canvas_actions import *
from .canvas_elements import *


class Canvas:

    def __init__(self, replay, send_queue):
        self._send_queue = send_queue
        self._replay = replay

        self._current_ref = 0
        self._ref_table = {}
        self._reset_actions()

        self.width = Config.config['gui']['width']
        self.height = Config.config['gui']['height']


    def _reset_actions(self):
        self._actions = CanvasAction([], [])


    def _get_ref(self, ref):
        ref_type = type(ref)
        if ref_type == str:
            return self._ref_table[ref]
        if ref_type == int:
            return ref
        raise TypeError("an integer or string is required")


    def _del_ref(self, ref):
        ref_type = type(ref)
        if ref_type == str:
            del self._ref_table[ref]
            return
        if ref_type == int:
            return
        raise TypeError("an integer or string is required")


    def initialize(self):
        self._store_all_images_data()
        self.resize_canvas(self.width, self.height)
        self.clear_canvas()
        self.apply_actions()


    def apply_actions(self):
        self._send_queue.put(self._actions)
        self._replay.store_message(self._actions)
        self._reset_actions()


    def add_action(self, action):
        act_type, act_payload = Parser.get_tuplestring(action)
        self._actions.action_types.append(act_type)
        self._actions.action_payloads.append(act_payload)


    # Actions

    def resize_canvas(self, width=None, height=None):
        self.width = width or self.width
        self.height = height or self.height
        self.add_action(
            ResizeCanvas(
                width = self.width,
                height = self.height
            )
        )


    def clear_canvas(self):
        self.add_action(ClearCanvas())


    def create_element(self, element, custom_ref=None):
        ref = self._current_ref
        self._current_ref += 1
        if custom_ref is not None:
            self._ref_table[custom_ref] = ref

        elm_type, elm_payload = Parser.get_tuplestring(element)
        self.add_action(
            CreateElement(
                ref = self._get_ref(ref),
                element_type = elm_type,
                element_payload = elm_payload
            )
        )

        return ref


    def edit_element(self, ref, element):
        elm_type, elm_payload = Parser.get_tuplestring(element)
        self.add_action(
            EditElement(
                self._get_ref(ref),
                element_type = elm_type,
                element_payload = elm_payload
            )
        )


    def delete_element(self, ref):
        self.add_action(
            DeleteElement(
                ref = self._get_ref(ref)
            )
        )
        self._del_ref(ref)


    def store_image_data(self, image_name, image_data):
        self.add_action(
            StoreImageData(
                image_name = image_name,
                image_data = image_data
            )
        )


    def _store_all_images_data(self):
        for name, path in Config.config['gui']['images'].items():
            with open(path, 'rb') as f:
                data = Parser.get_string(f.read())
                self.store_image_data(name, data)


    def bring_to_front(self, ref, target_ref=None):
        ref = self._get_ref(ref)
        if target_ref:
            target_ref = self._get_ref(target_ref)

        self.add_action(
            BringToFront(ref, target_ref)
        )


    def send_to_back(self, ref, target_ref=None):
        ref = self._get_ref(ref)
        if target_ref:
            target_ref = self._get_ref(target_ref)

        self.add_action(
            SendToBack(ref, target_ref)
        )


    # Elements

    def _create_element(self, element_class, element_kwargs, custom_ref):
        element_kwargs.pop('self')
        element_kwargs.pop('custom_ref')
        return self.create_element(element_class(**element_kwargs), custom_ref)


    def _edit_element(self, ref, element_class, element_kwargs):
        element_kwargs.pop('self')
        element_kwargs.pop('ref')
        self.edit_element(ref, element_class(**element_kwargs))


    @staticmethod
    def make_rgba(r, g, b, a):
        return Color(r, g, b, a)


    def create_circle(self, x, y, radius, color, stroke_width=None,
                      stroke_color=None, custom_ref=None):
        return self._create_element(Circle, locals(), custom_ref)


    def edit_circle(self, ref, x=None, y=None, radius=None, color=None,
                    stroke_width=None, stroke_color=None):
        self._edit_element(ref, Circle, locals())


    def create_ellipse(self, x, y, radius_x, radius_y, color, angle=None,
                       stroke_width=None, stroke_color=None, custom_ref=None):
        return self._create_element(Ellipse, locals(), custom_ref)


    def edit_ellipse(self, ref, x=None, y=None, radius_x=None, radius_y=None,
                     color=None, angle=None, stroke_width=None, stroke_color=None):
        self._edit_element(ref, Ellipse, locals())


    def create_rect(self, x, y, width, height, color, angle=None, center_origin=False,
                    stroke_width=None, stroke_color=None, custom_ref=None):
        return self._create_element(Rect, locals(), custom_ref)


    def edit_rect(self, ref, x=None, y=None, width=None, height=None, color=None,
                  angle=None, center_origin=None, stroke_width=None, stroke_color=None):
        self._edit_element(ref, Rect, locals())


    def create_line(self, x1, y1, x2, y2, color, stroke_width=None,
                    angle=None, custom_ref=None):
        return self._create_element(Line, locals(), custom_ref)


    def edit_line(self, ref, x1=None, y1=None, x2=None, y2=None,
                  color=None, stroke_width=None, angle=None):
        self._edit_element(ref, Line, locals())


    def create_polygon(self, x, y, color, offset_left=None, offset_top=None, angle=None,
                       center_origin=False, stroke_width=None, stroke_color=None,
                       custom_ref=None):
        return self._create_element(Polygon, locals(), custom_ref)


    def edit_polygon(self, ref, color=None, offset_left=None, offset_top=None,
                     angle=None, center_origin=None, stroke_width=None, stroke_color=None):
        self._edit_element(ref, Polygon, locals())


    def create_image(self, image_name, x, y,
                     scale_type=ScaleType.NoScale, scale_value=None, angle=None,
                     center_origin=False, stroke_width=None, stroke_color=None,
                     custom_ref=None):
        return self._create_element(Image, locals(), custom_ref)


    def edit_image(self, ref, x=None, y=None,
                   scale_type=None, scale_value=None, angle=None,
                   center_origin=None, stroke_width=None, stroke_color=None):
        self._edit_element(ref, Image, locals())


    def create_text(self, text, x, y, color, font_size, font_style=None, font=None,
                    background_color=None, angle=None, center_origin=None,
                    stroke_width=None, stroke_color=None, custom_ref=None):
        return self._create_element(Text, locals(), custom_ref)


    def edit_text(self, ref, x=None, y=None, color=None, font_size=None,
                  font_style=None, font=None, background_color=None, angle=None,
                  center_origin=None, stroke_width=None, stroke_color=None):
        self._edit_element(ref, Text, locals())
