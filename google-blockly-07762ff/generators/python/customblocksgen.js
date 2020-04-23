Blockly.Python['send'] = function (block) {
    var dropdown_button = block.getFieldValue('button');
    var number_name = block.getFieldValue('NAME');
    // TODO: Assemble Python into code variable.
    var poopblovk = "    send(\"";
    var peebliv = "\",";
    var beardfof = ")";
    var gamechar = poopblovk.concat(dropdown_button, peebliv, number_name, beardfof);
    var dysntart = "\n"
    var code = gamechar.concat(dysntart);
    return code;
};

Blockly.Python['start'] = function (block) {
    // TODO: Assemble Python into code variable.
    var code = 'import argparse\n' +
        'import serial\n' +
        'from time import sleep\n' +
        'import datetime\n' +
        '\n' +
        'parser = argparse.ArgumentParser()\n' +
        '\n' +
        'args = parser.parse_args()\n' +
        '\n' +
        '\n' +
        'class Special():\n' +
        '    RELEASE = "RELEASE"\n' +
        '\n' +
        '\n' +
        'class Button():\n' +
        '    A = "Button A"\n' +
        '    B = "Button B"\n' +
        '    X = "Button X"\n' +
        '    Y = "Button Y"\n' +
        '    L = "Button L"\n' +
        '    R = "Button R"\n' +
        '    ZL = "Button ZL"\n' +
        '    ZR = "Button ZR"\n' +
        '    HOME = "Button HOME"\n' +
        '    SELECT = "Button SELECT"\n' +
        '    START = "Button START"\n' +
        '    LCLICK = "Button LCLICK"\n' +
        '    RCLICK = "Button RCLICK"\n' +
        '    CAPTURE = "Button CAPTURE"\n' +
        '    RELEASE = "Button RELEASE"\n' +
        '\n' +
        '\n' +
        'class Hat():\n' +
        '    TOP = "HAT TOP"\n' +
        '    TOP_RIGHT = "HAT TOP_RIGHT"\n' +
        '    RIGHT = "HAT RIGHT"\n' +
        '    BOTTOM_RIGHT = "HAT BOTTOM_RIGHT"\n' +
        '    BOTTOM = "HAT BOTTOM"\n' +
        '    BOTTOM_LEFT = "HAT BOTTOM_LEFT"\n' +
        '    LEFT = "HAT LEFT"\n' +
        '    TOP_LEFT = "HAT TOP_LEFT"\n' +
        '    CENTER = "HAT CENTER"\n' +
        '\n' +
        '\n' +
        'class Joystick():\n' +
        '    UP = "UP"\n' +
        '    LEFT = "LX MIN"\n' +
        '    RIGHT = "RIGHT"\n' +
        '    DOWN = "DOWN"\n' +
        '\n' +
        '\n' +
        'def send(msg, duration=0):\n' +
        '    #print(f\'{datetime.datetime.now()} {msg}\')\n' +
        '    ser.write(f\'{msg}\\r\\n\'.encode(\'utf-8\'))\n' +
        '    sleep(duration)\n' +
        '    ser.write(b\'RELEASE\\r\\n\')\n' +
        '\n' +
        '\n' +
        'port = \'COM5\'\n' +
        'global ser\n' +
        'ser = serial.Serial(port, 9600)\n' +
        '\n' +
        '\n' +
        '# sleep(5)\n' +
        'def close():\n' +
        '    send(Button.A, 0.1)\n' +
        '    sleep(2)\n' +
        '    send(Button.HOME, 0.1)\n' +
        '    sleep(3)\n' +
        '    send(Button.X, 0.5)\n' +
        '    sleep(2)\n' +
        '    send(Button.A, 0.5)\n' +
        '    sleep(5)\n' +
        '\n' +
        '\n' +
        'def home():\n' +
        '    send(Button.HOME, 0.1)\n' +
        '    sleep(1)\n' +
        '\n' +
        'count = 0\n' +
        'try:\n' +
        '    while True:\n' +
        '       count = count + 1\n';
    return code;
};

Blockly.Python['end'] = function (block) {
    // TODO: Assemble Python into code variable.
    var code = 'except KeyboardInterrupt:\n' +
        '    send(\'RELEASE\')\n' +
        '    ser.close()';
    return code;
};

Blockly.Python['firsttime'] = function (block) {
    var number_times = block.getFieldValue('times');
    var statements_blocksinside = Blockly.Python.statementToCode(block, 'blocksinside');
    // TODO: Assemble Python into code variable.
    var adman = "    if count == "
    var madman = ":\n"
    var sadman = "        count=0"
    var badman = adman.concat(number_times, madman, statements_blocksinside)


    return badman;
};

