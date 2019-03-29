#!/usr/bin/python3

# speedometer
import wx
import wx.lib.agw.speedmeter as SM
from math import pi as pi

class DialMeter(SM.SpeedMeter):
    def __init__(self,  parent):
        SM.SpeedMeter.__init__(self, parent, agwStyle=SM.SM_DRAW_HAND|SM.SM_DRAW_SECTORS|SM.SM_DRAW_MIDDLE_TEXT|SM.SM_DRAW_SECONDARY_TICKS)
        
        # Set The Region Of Existence Of SpeedMeter (Always In Radians!!!!)

        # Create The Intervals That Will Divide Our SpeedMeter In Sectors
        intervals = range(0, 201, 20)
        self.SetIntervals(intervals)

        # Assign The Same Colours To All Sectors (We Simulate A Car Control For Speed)
        # Usually This Is Black
        colours = [wx.BLACK]*10
        self.SetIntervalColours(colours)

        # Assign The Ticks: Here They Are Simply The String Equivalent Of The Intervals
        ticks = [str(interval) for interval in intervals]
        self.SetTicks(ticks)
        # Set The Ticks/Tick Markers Colour
        self.SetTicksColour(wx.WHITE)
        # We Want To Draw 5 Secondary Ticks Between The Principal Ticks
        self.SetNumberOfSecondaryTicks(5)

        # Set The Font For The Ticks Markers
        self.SetTicksFont(wx.Font(7, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))

        # Set The Text In The Center Of SpeedMeter
        self.SetMiddleText("Km/h")
        # Assign The Colour To The Center Text
        self.SetMiddleTextColour(wx.WHITE)
        # Assign A Font To The Center Text
        self.SetMiddleTextFont(wx.Font(8, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        # Set The Colour For The Hand Indicator
        self.SetHandColour(wx.Colour(255, 50, 0))

        # Do Not Draw The External (Container) Arc. Drawing The External Arc May
        # Sometimes Create Uglier Controls. Try To Comment This Line And See It
        # For Yourself!
        self.DrawExternalArc(False)

        # Set The Current Value For The SpeedMeter
        self.SetSpeedValue(44)

