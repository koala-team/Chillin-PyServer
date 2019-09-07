# -*- coding: utf-8 -*-


class ReferenceManager:

    def __init__(self):
        self._current_ref = 0
        self._all_refs = []
        self._custom_ref_table = {}

        self.new('MainCamera')


    def new(self, custom_ref=None):
        if custom_ref is not None:
            if custom_ref in self._custom_ref_table:
                raise ValueError("custom_ref '%s' already exists" % custom_ref)

        ref = self._current_ref
        self._current_ref += 1
        self._all_refs.append(ref)
        if custom_ref is not None:
            self._custom_ref_table[custom_ref] = ref
        return ref


    def get(self, custom_ref):
        return self._custom_ref_table[custom_ref]


    def remove(self, ref):
        for custom_ref in self._custom_ref_table.keys():
            if self._custom_ref_table[custom_ref] == ref:
                del self._custom_ref_table[custom_ref]
        self._all_refs.remove(ref)


    def remove_custom_ref(self, custom_ref):
        ref = self._custom_ref_table[custom_ref]
        del self._custom_ref_table[custom_ref]
        return ref


    def exists(self, ref):
        return ref in self._all_refs


    def exists_custom_ref(self, custom_ref):    
        return custom_ref in self._custom_ref_table


default_reference_manager = ReferenceManager()
