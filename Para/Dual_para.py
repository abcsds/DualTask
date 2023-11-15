#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on noviembre 15, 2023, at 10:22
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = 'Dual_para'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='D:\\Users\\Administrativo\\Documents\\GitHub\\DualTask\\Para\\Dual_para.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.EXP)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1366, 768], fullscr=True, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='pix'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'pix'
    win.mouseVisible = False
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='iohub')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='ioHub')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Welcome_screen__2" ---
    Welcome = visual.TextStim(win=win, name='Welcome',
        text='Bienvenido ',
        font='Open Sans',
        pos=(0, 0), height=36.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Instruccions" ---
    Instrucccions = visual.TextStim(win=win, name='Instrucccions',
        text='A continuación presione la barra espaciadora para comenzar el experimento.  \n\n',
        font='Open Sans',
        pos=(0, 0), height=36.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "Blank" ---
    Blank_1 = visual.TextStim(win=win, name='Blank_1',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=36.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Instruction_2" ---
    text = visual.TextStim(win=win, name='text',
        text='Sigue el circulo con el mouse ',
        font='Open Sans',
        pos=(0, 0), height=36.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_2 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "Circle" ---
    # Run 'Begin Experiment' code from code
    #import random
    from numpy import random
    import math
    import psychopy.logging as log
    
    # Function to calculate distance between two points
    def distance(point1, point2):
        return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5
        
    def rad2grad(rad):
        return rad*180/math.pi
        
    def grad2rad(grad):
        return grad*math.pi/180
        
    def angle2origin (pos):
        if pos[0] * pos[1] >= 0: 
            angle = math.atan(pos[1] / pos[0]) + math.pi 
        else:
            angle = math.atan(pos[1] / pos[0])
        return angle 
    
    # Define size of the circle
    circle_radius = 10
    circle_speed = 15
    circle_pos = [0,0]
    circle_direction = random.uniform(0, 2 * math.pi)  # Initial direction (random)
    angle_uncertainty = math.pi/2
    
    cross_color = "white"
    
    # Define boundaries
    boundary_x_min = -win.size[0] / 2 + circle_radius
    boundary_x_max = win.size[0] / 2 - circle_radius
    boundary_y_min = -win.size[1] / 2 + circle_radius
    boundary_y_max = win.size[1] / 2 - circle_radius
    
    # Define la duración del estímulo 
    stimulus_duration = 0.5 
    
    # promedio de las duraciones entre estimulos
    between_stimuli = 2.0
    
    # define square_pos
    square_pos = (0,0)
    
    # proportion of x in list of all letters 
    n_x = 1
    circle = visual.ShapeStim(
        win=win, name='circle',
        size=(circle_radius*2, circle_radius*2), vertices='circle',
        ori=0.0, pos=[0,0], anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    mouse = event.Mouse(win=win)
    x, y = [None, None]
    mouse.mouseClock = core.Clock()
    fixation_cross = visual.TextStim(win=win, name='fixation_cross',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=48.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    Letter = visual.TextStim(win=win, name='Letter',
        text='',
        font='Open Sans',
        pos=(0, 0), height=48.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    square = visual.Rect(
        win=win, name='square',
        width=(40, 40)[0], height=(40, 40)[1],
        ori=0.0, pos=[0,0], anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='transparent',
        opacity=None, depth=-5.0, interpolate=True)
    
    # --- Initialize components for Routine "NasaTLX" ---
    text_mental_demand = visual.TextStim(win=win, name='text_mental_demand',
        text='Exigencia mental',
        font='Open Sans',
        pos=(-480, 400), height=48.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    slider_mental_demand = visual.Slider(win=win, name='slider_mental_demand',
        startValue=None, size=(480, 10), pos=(-480, 270), units=win.units,
        labels=("Baja", "", "Alta"), ticks=(-10, 0, 10), granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=36.0,
        flip=False, ori=0.0, depth=-1, readOnly=False)
    text_fisical_demand = visual.TextStim(win=win, name='text_fisical_demand',
        text='Exigencia física',
        font='Open Sans',
        pos=(-480, 80), height=48.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    slider_fisical_demand = visual.Slider(win=win, name='slider_fisical_demand',
        startValue=None, size=(480, 10), pos=(-480, -70), units=win.units,
        labels=("Baja", "", "Alta"), ticks=(-10, 0, 10), granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=36.0,
        flip=False, ori=0.0, depth=-3, readOnly=False)
    text_temporal_demand = visual.TextStim(win=win, name='text_temporal_demand',
        text='Exigencia temporal',
        font='Open Sans',
        pos=(-480, -270), height=48.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    sider_temporal_demand = visual.Slider(win=win, name='sider_temporal_demand',
        startValue=None, size=(480, 10), pos=(-480, -360), units=win.units,
        labels=("Baja", "", "Alta"), ticks=(-10, 0, 10), granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=36.0,
        flip=False, ori=0.0, depth=-5, readOnly=False)
    text_effort_demand = visual.TextStim(win=win, name='text_effort_demand',
        text='Exigencia eficiencia',
        font='Open Sans',
        pos=(480, 400), height=48.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    slider_effort_demand = visual.Slider(win=win, name='slider_effort_demand',
        startValue=None, size=(480, 10), pos=(480, 270), units=win.units,
        labels=("Baja", "", "Alta"), ticks=(-10, 0, 10), granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=36.0,
        flip=False, ori=0.0, depth=-7, readOnly=False)
    text_performance_demand = visual.TextStim(win=win, name='text_performance_demand',
        text='Exigencia rendimiento',
        font='Open Sans',
        pos=(480, 80), height=48.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-8.0);
    slider_performance_demand = visual.Slider(win=win, name='slider_performance_demand',
        startValue=None, size=(480, 10), pos=(480, -70), units=win.units,
        labels=("Baja", "", "Alta"), ticks=(-10, 0, 10), granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=36.0,
        flip=False, ori=0.0, depth=-9, readOnly=False)
    text_frustation_demand = visual.TextStim(win=win, name='text_frustation_demand',
        text='Exigencia frustración',
        font='Open Sans',
        pos=(480, -270), height=48.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-10.0);
    slider_frustation_demand = visual.Slider(win=win, name='slider_frustation_demand',
        startValue=None, size=(480, 10), pos=(480, -360), units=win.units,
        labels=("Baja", "", "Alta"), ticks=(-10, 0, 10), granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=36.0,
        flip=False, ori=0.0, depth=-11, readOnly=False)
    key_resp_3 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "Pause" ---
    text_pause = visual.TextStim(win=win, name='text_pause',
        text=f"""Este es el fin del ensayo X de 5
    
    [Presiona barra espaciadora para contiunar]
    """,
        font='Open Sans',
        pos=(0, 0), height=64.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "End" ---
    Terminado = visual.TextStim(win=win, name='Terminado',
        text='End',
        font='Open Sans',
        pos=(0, 0), height=36.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "Welcome_screen__2" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Welcome_screen__2.started', globalClock.getTime())
    # keep track of which components have finished
    Welcome_screen__2Components = [Welcome]
    for thisComponent in Welcome_screen__2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Welcome_screen__2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Welcome* updates
        
        # if Welcome is starting this frame...
        if Welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Welcome.frameNStart = frameN  # exact frame index
            Welcome.tStart = t  # local t and not account for scr refresh
            Welcome.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Welcome, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Welcome.started')
            # update status
            Welcome.status = STARTED
            Welcome.setAutoDraw(True)
        
        # if Welcome is active this frame...
        if Welcome.status == STARTED:
            # update params
            pass
        
        # if Welcome is stopping this frame...
        if Welcome.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Welcome.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Welcome.tStop = t  # not accounting for scr refresh
                Welcome.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Welcome.stopped')
                # update status
                Welcome.status = FINISHED
                Welcome.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Welcome_screen__2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Welcome_screen__2" ---
    for thisComponent in Welcome_screen__2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Welcome_screen__2.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "Instruccions" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Instruccions.started', globalClock.getTime())
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    InstruccionsComponents = [Instrucccions, key_resp]
    for thisComponent in InstruccionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instruccions" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Instrucccions* updates
        
        # if Instrucccions is starting this frame...
        if Instrucccions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instrucccions.frameNStart = frameN  # exact frame index
            Instrucccions.tStart = t  # local t and not account for scr refresh
            Instrucccions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instrucccions, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instrucccions.started')
            # update status
            Instrucccions.status = STARTED
            Instrucccions.setAutoDraw(True)
        
        # if Instrucccions is active this frame...
        if Instrucccions.status == STARTED:
            # update params
            pass
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstruccionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instruccions" ---
    for thisComponent in InstruccionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Instruccions.stopped', globalClock.getTime())
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    thisExp.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        thisExp.addData('key_resp.rt', key_resp.rt)
        thisExp.addData('key_resp.duration', key_resp.duration)
    thisExp.nextEntry()
    # the Routine "Instruccions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Blank" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Blank.started', globalClock.getTime())
    # keep track of which components have finished
    BlankComponents = [Blank_1]
    for thisComponent in BlankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Blank" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Blank_1* updates
        
        # if Blank_1 is starting this frame...
        if Blank_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Blank_1.frameNStart = frameN  # exact frame index
            Blank_1.tStart = t  # local t and not account for scr refresh
            Blank_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Blank_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Blank_1.started')
            # update status
            Blank_1.status = STARTED
            Blank_1.setAutoDraw(True)
        
        # if Blank_1 is active this frame...
        if Blank_1.status == STARTED:
            # update params
            pass
        
        # if Blank_1 is stopping this frame...
        if Blank_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Blank_1.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                Blank_1.tStop = t  # not accounting for scr refresh
                Blank_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Blank_1.stopped')
                # update status
                Blank_1.status = FINISHED
                Blank_1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Blank" ---
    for thisComponent in BlankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Blank.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    
    # --- Prepare to start Routine "Instruction_2" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Instruction_2.started', globalClock.getTime())
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    Instruction_2Components = [text, key_resp_2]
    for thisComponent in Instruction_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instruction_2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # *key_resp_2* updates
        waitOnFlip = False
        
        # if key_resp_2 is starting this frame...
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_2.started')
            # update status
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                key_resp_2.duration = _key_resp_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instruction_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instruction_2" ---
    for thisComponent in Instruction_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Instruction_2.stopped', globalClock.getTime())
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    thisExp.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        thisExp.addData('key_resp_2.rt', key_resp_2.rt)
        thisExp.addData('key_resp_2.duration', key_resp_2.duration)
    thisExp.nextEntry()
    # the Routine "Instruction_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=5.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    
    for thisTrial in trials:
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "Circle" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Circle.started', globalClock.getTime())
        # Run 'Begin Routine' code from code
        next_flash_time = core.getTime() + stimulus_duration + random.normal(loc=between_stimuli, scale=1) + 1 # Initial flash time
        
        stimulus = "X"
        all_letters = ["M", "N", "Y", "A", "U", "H"]
        
        all_letters = all_letters + (["X"] * n_x)
        print (all_letters) 
        
        last_flash_time = None 
        offset_time = core.getTime() + stimulus_duration
        
        # Set the mouse at the center of the screen
        mouse.setPos([0,0])
        
        # Log the trial number
        log.exp(f"Trial begin: {trials.thisN+1}")
        
        # setup some python lists for storing info about the mouse
        mouse.x = []
        mouse.y = []
        mouse.leftButton = []
        mouse.midButton = []
        mouse.rightButton = []
        mouse.time = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        CircleComponents = [circle, mouse, fixation_cross, Letter, square]
        for thisComponent in CircleComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Circle" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 60.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code
            # Calculate the new position based on speed and direction
            circle_pos[0] += circle_speed * math.cos(circle_direction)
            circle_pos[1] += circle_speed * math.sin(circle_direction)
            
            
            # Check for collisions with boundaries
            if circle_pos[0] <= boundary_x_min or circle_pos[0] >= boundary_x_max:
                circle_direction = math.pi - circle_direction
            if circle_pos[1] <= boundary_y_min or circle_pos[1] >= boundary_y_max:
                circle_direction = -circle_direction
            
            # Randomly adjust speed and direction
            # chance of changing direction on every frame
            if random.random() < 0.2:  # 20% chance of speed change on every frame
                # circle_speed = random.uniform(5, 20)
                circle_direction += random.uniform(-angle_uncertainty/2, angle_uncertainty/2)
             
            mouse_pos = mouse.getPos()
            dist = distance(mouse_pos, circle.pos)
            log.exp(f"Distance = {dist}")
            
            # Update figure color based on distance (adjust the values)
            # if dist < 100:
                # circle.fillColor = "green"
            # elif dist < 200:
                #circle.fillColor = "yellow"
            # else:
                # circle.fillColor = "red"
            
            # Update figure color based on distance (adjust the values)
            if dist < 100:
                square.borderColor = "limegreen"
            elif dist < 200:
                square.borderColor = "yellow"
            else:
                square.borderColor = "red"
                
            # print(stimulus)
            
            # Check for fixation cross flash
            if core.getTime() >= next_flash_time:
                last_flash_time = next_flash_time
                stimulus = random.choice(all_letters)
                win.flip()
                log.exp(f"New stimulus letter: {stimulus}")
                next_flash_time = core.getTime() + stimulus_duration + random.normal(loc=between_stimuli, scale=1)  # Schedule the next flash
                offset_time = last_flash_time + stimulus_duration
                print(offset_time)
                
            if core.getTime() >= offset_time:
               stimulus = ""
               win.flip()
               log.exp(f"Removed stimulus letter")
               
            # Check square new position bassed of mouse direction 
            square_pos = mouse.getPos()
            
            
              
            
            
            # *circle* updates
            
            # if circle is starting this frame...
            if circle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle.frameNStart = frameN  # exact frame index
                circle.tStart = t  # local t and not account for scr refresh
                circle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'circle.started')
                # update status
                circle.status = STARTED
                circle.setAutoDraw(True)
            
            # if circle is active this frame...
            if circle.status == STARTED:
                # update params
                circle.setPos(circle_pos, log=False)
            
            # if circle is stopping this frame...
            if circle.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circle.tStartRefresh + 60-frameTolerance:
                    # keep track of stop time/frame for later
                    circle.tStop = t  # not accounting for scr refresh
                    circle.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'circle.stopped')
                    # update status
                    circle.status = FINISHED
                    circle.setAutoDraw(False)
            # *mouse* updates
            
            # if mouse is starting this frame...
            if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse.started', t)
                # update status
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            
            # if mouse is stopping this frame...
            if mouse.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > mouse.tStartRefresh + 60-frameTolerance:
                    # keep track of stop time/frame for later
                    mouse.tStop = t  # not accounting for scr refresh
                    mouse.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.addData('mouse.stopped', t)
                    # update status
                    mouse.status = FINISHED
            if mouse.status == STARTED:  # only update if started and not finished!
                buttons = mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        x, y = mouse.getPos()
                        mouse.x.append(x)
                        mouse.y.append(y)
                        buttons = mouse.getPressed()
                        mouse.leftButton.append(buttons[0])
                        mouse.midButton.append(buttons[1])
                        mouse.rightButton.append(buttons[2])
                        mouse.time.append(mouse.mouseClock.getTime())
            
            # *fixation_cross* updates
            
            # if fixation_cross is starting this frame...
            if fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_cross.frameNStart = frameN  # exact frame index
                fixation_cross.tStart = t  # local t and not account for scr refresh
                fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_cross.started')
                # update status
                fixation_cross.status = STARTED
                fixation_cross.setAutoDraw(True)
            
            # if fixation_cross is active this frame...
            if fixation_cross.status == STARTED:
                # update params
                fixation_cross.setColor(cross_color, colorSpace='rgb', log=False)
            
            # if fixation_cross is stopping this frame...
            if fixation_cross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_cross.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_cross.tStop = t  # not accounting for scr refresh
                    fixation_cross.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_cross.stopped')
                    # update status
                    fixation_cross.status = FINISHED
                    fixation_cross.setAutoDraw(False)
            
            # *Letter* updates
            
            # if Letter is starting this frame...
            if Letter.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                Letter.frameNStart = frameN  # exact frame index
                Letter.tStart = t  # local t and not account for scr refresh
                Letter.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Letter, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Letter.started')
                # update status
                Letter.status = STARTED
                Letter.setAutoDraw(True)
            
            # if Letter is active this frame...
            if Letter.status == STARTED:
                # update params
                Letter.setText(stimulus, log=False)
            
            # if Letter is stopping this frame...
            if Letter.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Letter.tStartRefresh + 59-frameTolerance:
                    # keep track of stop time/frame for later
                    Letter.tStop = t  # not accounting for scr refresh
                    Letter.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Letter.stopped')
                    # update status
                    Letter.status = FINISHED
                    Letter.setAutoDraw(False)
            
            # *square* updates
            
            # if square is starting this frame...
            if square.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                square.frameNStart = frameN  # exact frame index
                square.tStart = t  # local t and not account for scr refresh
                square.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'square.started')
                # update status
                square.status = STARTED
                square.setAutoDraw(True)
            
            # if square is active this frame...
            if square.status == STARTED:
                # update params
                square.setPos(square_pos, log=False)
            
            # if square is stopping this frame...
            if square.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > square.tStartRefresh + 60-frameTolerance:
                    # keep track of stop time/frame for later
                    square.tStop = t  # not accounting for scr refresh
                    square.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'square.stopped')
                    # update status
                    square.status = FINISHED
                    square.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in CircleComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Circle" ---
        for thisComponent in CircleComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Circle.stopped', globalClock.getTime())
        # store data for trials (TrialHandler)
        trials.addData('mouse.x', mouse.x)
        trials.addData('mouse.y', mouse.y)
        trials.addData('mouse.leftButton', mouse.leftButton)
        trials.addData('mouse.midButton', mouse.midButton)
        trials.addData('mouse.rightButton', mouse.rightButton)
        trials.addData('mouse.time', mouse.time)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-60.000000)
        
        # --- Prepare to start Routine "NasaTLX" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('NasaTLX.started', globalClock.getTime())
        slider_mental_demand.reset()
        slider_fisical_demand.reset()
        sider_temporal_demand.reset()
        slider_effort_demand.reset()
        slider_performance_demand.reset()
        slider_frustation_demand.reset()
        key_resp_3.keys = []
        key_resp_3.rt = []
        _key_resp_3_allKeys = []
        # keep track of which components have finished
        NasaTLXComponents = [text_mental_demand, slider_mental_demand, text_fisical_demand, slider_fisical_demand, text_temporal_demand, sider_temporal_demand, text_effort_demand, slider_effort_demand, text_performance_demand, slider_performance_demand, text_frustation_demand, slider_frustation_demand, key_resp_3]
        for thisComponent in NasaTLXComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "NasaTLX" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_mental_demand* updates
            
            # if text_mental_demand is starting this frame...
            if text_mental_demand.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_mental_demand.frameNStart = frameN  # exact frame index
                text_mental_demand.tStart = t  # local t and not account for scr refresh
                text_mental_demand.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_mental_demand, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_mental_demand.started')
                # update status
                text_mental_demand.status = STARTED
                text_mental_demand.setAutoDraw(True)
            
            # if text_mental_demand is active this frame...
            if text_mental_demand.status == STARTED:
                # update params
                pass
            
            # *slider_mental_demand* updates
            
            # if slider_mental_demand is starting this frame...
            if slider_mental_demand.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider_mental_demand.frameNStart = frameN  # exact frame index
                slider_mental_demand.tStart = t  # local t and not account for scr refresh
                slider_mental_demand.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider_mental_demand, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_mental_demand.started')
                # update status
                slider_mental_demand.status = STARTED
                slider_mental_demand.setAutoDraw(True)
            
            # if slider_mental_demand is active this frame...
            if slider_mental_demand.status == STARTED:
                # update params
                pass
            
            # *text_fisical_demand* updates
            
            # if text_fisical_demand is starting this frame...
            if text_fisical_demand.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_fisical_demand.frameNStart = frameN  # exact frame index
                text_fisical_demand.tStart = t  # local t and not account for scr refresh
                text_fisical_demand.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_fisical_demand, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_fisical_demand.started')
                # update status
                text_fisical_demand.status = STARTED
                text_fisical_demand.setAutoDraw(True)
            
            # if text_fisical_demand is active this frame...
            if text_fisical_demand.status == STARTED:
                # update params
                pass
            
            # *slider_fisical_demand* updates
            
            # if slider_fisical_demand is starting this frame...
            if slider_fisical_demand.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider_fisical_demand.frameNStart = frameN  # exact frame index
                slider_fisical_demand.tStart = t  # local t and not account for scr refresh
                slider_fisical_demand.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider_fisical_demand, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_fisical_demand.started')
                # update status
                slider_fisical_demand.status = STARTED
                slider_fisical_demand.setAutoDraw(True)
            
            # if slider_fisical_demand is active this frame...
            if slider_fisical_demand.status == STARTED:
                # update params
                pass
            
            # *text_temporal_demand* updates
            
            # if text_temporal_demand is starting this frame...
            if text_temporal_demand.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_temporal_demand.frameNStart = frameN  # exact frame index
                text_temporal_demand.tStart = t  # local t and not account for scr refresh
                text_temporal_demand.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_temporal_demand, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_temporal_demand.started')
                # update status
                text_temporal_demand.status = STARTED
                text_temporal_demand.setAutoDraw(True)
            
            # if text_temporal_demand is active this frame...
            if text_temporal_demand.status == STARTED:
                # update params
                pass
            
            # *sider_temporal_demand* updates
            
            # if sider_temporal_demand is starting this frame...
            if sider_temporal_demand.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sider_temporal_demand.frameNStart = frameN  # exact frame index
                sider_temporal_demand.tStart = t  # local t and not account for scr refresh
                sider_temporal_demand.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sider_temporal_demand, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sider_temporal_demand.started')
                # update status
                sider_temporal_demand.status = STARTED
                sider_temporal_demand.setAutoDraw(True)
            
            # if sider_temporal_demand is active this frame...
            if sider_temporal_demand.status == STARTED:
                # update params
                pass
            
            # *text_effort_demand* updates
            
            # if text_effort_demand is starting this frame...
            if text_effort_demand.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_effort_demand.frameNStart = frameN  # exact frame index
                text_effort_demand.tStart = t  # local t and not account for scr refresh
                text_effort_demand.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_effort_demand, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_effort_demand.started')
                # update status
                text_effort_demand.status = STARTED
                text_effort_demand.setAutoDraw(True)
            
            # if text_effort_demand is active this frame...
            if text_effort_demand.status == STARTED:
                # update params
                pass
            
            # *slider_effort_demand* updates
            
            # if slider_effort_demand is starting this frame...
            if slider_effort_demand.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider_effort_demand.frameNStart = frameN  # exact frame index
                slider_effort_demand.tStart = t  # local t and not account for scr refresh
                slider_effort_demand.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider_effort_demand, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_effort_demand.started')
                # update status
                slider_effort_demand.status = STARTED
                slider_effort_demand.setAutoDraw(True)
            
            # if slider_effort_demand is active this frame...
            if slider_effort_demand.status == STARTED:
                # update params
                pass
            
            # *text_performance_demand* updates
            
            # if text_performance_demand is starting this frame...
            if text_performance_demand.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_performance_demand.frameNStart = frameN  # exact frame index
                text_performance_demand.tStart = t  # local t and not account for scr refresh
                text_performance_demand.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_performance_demand, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_performance_demand.started')
                # update status
                text_performance_demand.status = STARTED
                text_performance_demand.setAutoDraw(True)
            
            # if text_performance_demand is active this frame...
            if text_performance_demand.status == STARTED:
                # update params
                pass
            
            # *slider_performance_demand* updates
            
            # if slider_performance_demand is starting this frame...
            if slider_performance_demand.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider_performance_demand.frameNStart = frameN  # exact frame index
                slider_performance_demand.tStart = t  # local t and not account for scr refresh
                slider_performance_demand.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider_performance_demand, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_performance_demand.started')
                # update status
                slider_performance_demand.status = STARTED
                slider_performance_demand.setAutoDraw(True)
            
            # if slider_performance_demand is active this frame...
            if slider_performance_demand.status == STARTED:
                # update params
                pass
            
            # *text_frustation_demand* updates
            
            # if text_frustation_demand is starting this frame...
            if text_frustation_demand.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_frustation_demand.frameNStart = frameN  # exact frame index
                text_frustation_demand.tStart = t  # local t and not account for scr refresh
                text_frustation_demand.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_frustation_demand, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_frustation_demand.started')
                # update status
                text_frustation_demand.status = STARTED
                text_frustation_demand.setAutoDraw(True)
            
            # if text_frustation_demand is active this frame...
            if text_frustation_demand.status == STARTED:
                # update params
                pass
            
            # *slider_frustation_demand* updates
            
            # if slider_frustation_demand is starting this frame...
            if slider_frustation_demand.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider_frustation_demand.frameNStart = frameN  # exact frame index
                slider_frustation_demand.tStart = t  # local t and not account for scr refresh
                slider_frustation_demand.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider_frustation_demand, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_frustation_demand.started')
                # update status
                slider_frustation_demand.status = STARTED
                slider_frustation_demand.setAutoDraw(True)
            
            # if slider_frustation_demand is active this frame...
            if slider_frustation_demand.status == STARTED:
                # update params
                pass
            
            # *key_resp_3* updates
            waitOnFlip = False
            
            # if key_resp_3 is starting this frame...
            if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_3.frameNStart = frameN  # exact frame index
                key_resp_3.tStart = t  # local t and not account for scr refresh
                key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_3.started')
                # update status
                key_resp_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_3.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_3.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_3_allKeys.extend(theseKeys)
                if len(_key_resp_3_allKeys):
                    key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                    key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                    key_resp_3.duration = _key_resp_3_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in NasaTLXComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "NasaTLX" ---
        for thisComponent in NasaTLXComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('NasaTLX.stopped', globalClock.getTime())
        trials.addData('slider_mental_demand.response', slider_mental_demand.getRating())
        trials.addData('slider_mental_demand.rt', slider_mental_demand.getRT())
        trials.addData('slider_fisical_demand.response', slider_fisical_demand.getRating())
        trials.addData('slider_fisical_demand.rt', slider_fisical_demand.getRT())
        trials.addData('sider_temporal_demand.response', sider_temporal_demand.getRating())
        trials.addData('sider_temporal_demand.rt', sider_temporal_demand.getRT())
        trials.addData('slider_effort_demand.response', slider_effort_demand.getRating())
        trials.addData('slider_effort_demand.rt', slider_effort_demand.getRT())
        trials.addData('slider_performance_demand.response', slider_performance_demand.getRating())
        trials.addData('slider_performance_demand.rt', slider_performance_demand.getRT())
        trials.addData('slider_frustation_demand.response', slider_frustation_demand.getRating())
        trials.addData('slider_frustation_demand.rt', slider_frustation_demand.getRT())
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
            key_resp_3.keys = None
        trials.addData('key_resp_3.keys',key_resp_3.keys)
        if key_resp_3.keys != None:  # we had a response
            trials.addData('key_resp_3.rt', key_resp_3.rt)
            trials.addData('key_resp_3.duration', key_resp_3.duration)
        # the Routine "NasaTLX" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Pause" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Pause.started', globalClock.getTime())
        # keep track of which components have finished
        PauseComponents = [text_pause]
        for thisComponent in PauseComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Pause" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_pause* updates
            
            # if text_pause is starting this frame...
            if text_pause.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_pause.frameNStart = frameN  # exact frame index
                text_pause.tStart = t  # local t and not account for scr refresh
                text_pause.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_pause, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_pause.started')
                # update status
                text_pause.status = STARTED
                text_pause.setAutoDraw(True)
            
            # if text_pause is active this frame...
            if text_pause.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PauseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Pause" ---
        for thisComponent in PauseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Pause.stopped', globalClock.getTime())
        # the Routine "Pause" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 5.0 repeats of 'trials'
    
    
    # --- Prepare to start Routine "End" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('End.started', globalClock.getTime())
    # keep track of which components have finished
    EndComponents = [Terminado]
    for thisComponent in EndComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "End" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Terminado* updates
        
        # if Terminado is starting this frame...
        if Terminado.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Terminado.frameNStart = frameN  # exact frame index
            Terminado.tStart = t  # local t and not account for scr refresh
            Terminado.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Terminado, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Terminado.started')
            # update status
            Terminado.status = STARTED
            Terminado.setAutoDraw(True)
        
        # if Terminado is active this frame...
        if Terminado.status == STARTED:
            # update params
            pass
        
        # if Terminado is stopping this frame...
        if Terminado.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Terminado.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Terminado.tStop = t  # not accounting for scr refresh
                Terminado.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Terminado.stopped')
                # update status
                Terminado.status = FINISHED
                Terminado.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EndComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "End" ---
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('End.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
