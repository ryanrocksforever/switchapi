Blockly.Blocks['send'] = {
    init: function () {
        this.appendDummyInput()
            .appendField(new Blockly.FieldDropdown([["Button B", "Button B"], ["Button A", "Button A"], ["Button X", "Button X"], ["Button Y", "Button Y"], ["Button L", "Button L"], ["Button R", "Button R"], ["Button ZL", "Button ZL"], ["Button ZR", "Button ZR"], ["Button HOME", "Button HOME"], ["Button SELECT", "Button SELECT"], ["Button LCLICK", "Button LCLICK"], ["Button RCLICK", "Button RCLICK"], ["Button CAPTURE", "Button CAPTURE"], ["Button RELEASE", "Button RELEASE"], ["HAT TOP", "HAT TOP"], ["HAT TOP_RIGHT", "HAT TOP_RIGHT"], ["HAT RIGHT", "HAT RIGHT"], ["HAT BOTTOM_RIGHT", "HAT BOTTOM_RIGHT"], ["HAT BOTTOM", "HAT BOTTOM"], ["HAT BOTTOM_LEFT", "HAT BOTTOM_LEFT"], ["HAT LEFT", "HAT LEFT"], ["HAT TOP_LEFT", "HAT TOP_LEFT"], ["HAT CENTER", "HAT CENTER"], ["HAT CENTER", "HAT CENTER"], ["L Joystick UP", "LY MIN"], ["L Joystick DOWN", "LY MAX"], ["L Joystick RIGHT", "LX MAX"], ["L Joystick LEFT", "LX MIN"], ["R Joystick UP", "RY MIN"], ["R Joystick DOWN", "RY MAX"], ["R Joystick LEFT", "RX MIN"], ["R Joystick RIGHT", "RX MAX"], ["None", "None"]]), "button")
            .appendField(new Blockly.FieldNumber(0.1, 0), "NAME");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(230);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['start'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("Start");
        this.setNextStatement(true, null);
        this.setColour(230);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['end'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("End");
        this.setPreviousStatement(true, null);
        this.setColour(230);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['firsttime'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("Do Every")
            .appendField(new Blockly.FieldNumber(0, 0), "times")
            .appendField("loops");
        this.appendStatementInput("blocksinside")
            .setCheck(null);
        this.setInputsInline(false);
        this.setPreviousStatement(true, "start");
        this.setNextStatement(true, null);
        this.setColour(230);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};