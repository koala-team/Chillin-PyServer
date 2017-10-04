#! /usr/bin/env python
# -*- coding: utf-8 -*-

from koala_serializer import generate

generate('ks/commands.ks', 'python', 'ks')
generate('ks/models.ks', 'python', 'ks')
