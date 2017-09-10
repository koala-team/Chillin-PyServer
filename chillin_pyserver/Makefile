# Makefile

.PHONY: all gen gen_gui

KOALASC = koalasc
PROG_LANG = python

MESSAGE_SRC = "helpers/messages.ks"
GENERATED_MESSAGE_DIR = "helpers"

GUI_MESSAGE_SRC = "gui/messages.ks"
GUI_CANACT_SRC = "gui/canvas_actions.ks"
GUI_CANELM_SRC = "gui/canvas_elements.ks"
GUI_GENERATED_MESSAGE_DIR = "gui"


all: gen gen_gui

gen:
	$(KOALASC) $(MESSAGE_SRC) $(PROG_LANG) $(GENERATED_MESSAGE_DIR)


gen_gui:
	$(KOALASC) $(GUI_MESSAGE_SRC) $(PROG_LANG) $(GUI_GENERATED_MESSAGE_DIR)
	$(KOALASC) $(GUI_CANACT_SRC) $(PROG_LANG) $(GUI_GENERATED_MESSAGE_DIR)
	$(KOALASC) $(GUI_CANELM_SRC) $(PROG_LANG) $(GUI_GENERATED_MESSAGE_DIR)
