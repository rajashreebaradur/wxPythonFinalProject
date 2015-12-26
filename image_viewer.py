import wx

# Frame subclassed from wx.Frame
class Frame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title=title, size=(400,250), style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER) # Set frame size and disable frame resizing
        self.Center()
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('Light Grey')

        self.CreateMenuBar()

    # Create a new instance of menuBar
    def CreateMenuBar(self):
        menuBar = wx.MenuBar()
        self.SetMenuBar(menuBar)
        menuFile = wx.Menu()
        menuBar.Append(menuFile, "&File")
        

# Create a new app
class App(wx.App):
    def OnInit(self):
        self.frame = Frame(None, -1, "Image Viewer")
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ == "__main__":
    app = App(redirect=True) # Redirect stdout/stderr to a window

    app.MainLoop()
