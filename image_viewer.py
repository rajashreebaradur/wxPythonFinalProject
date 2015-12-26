import wx
import os

# Frame subclassed from wx.Frame
class Frame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title=title, size=(400,250), style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER) # Set frame size and disable frame resizing
        self.Center()
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('Light Grey')

        self.CreateMenuBar()

        # Create a StatusBar
        self.StatusBar = self.CreateStatusBar()
        self.StatusBar.SetFieldsCount(2)
        self.StatusBar.SetStatusText('No Image Specified', 1)

        self.bitmap = None # set to None as it is referred in ShowBitmap before it is instantiated

    # Create a new instance of menuBar
    def CreateMenuBar(self):
        menuBar = wx.MenuBar()
        self.SetMenuBar(menuBar)
        menuFile = wx.Menu()
        menuBar.Append(menuFile, "&File")
        fileOpenMenuItem = menuFile.Append(-1, "&Open...\tCtrl+O", "Open an image")
        self.Bind(wx.EVT_MENU, self.OnOpen, fileOpenMenuItem)

        exitMenuItem = menuFile.Append(-1, "E&xit\tCtrl+Q", "Exit the application")
        self.Bind(wx.EVT_MENU, self.OnExit, exitMenuItem)

    def OnOpen(self, event):
        "Open an image file, set title if successful"
        #print "OnOpen called"
        
        # Create a file-open dialog in the current working directory
        filters = 'Image files(*.gif;*.png;*.jpg)|*.gif;*.png;*.jpg'
        dlg = wx.FileDialog(self,
                      message="Open an image...",
                      defaultDir=os.getcwd(),
                      defaultFile="",
                      wildcard=filters,
                      style=wx.OPEN)

        # Call the dialog as a model-dialog so we are required to choose Ok or Cancel
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetPath() # If user has selected something, get the file path and set the window's title to the path
            #print filename
            self.SetTitle(filename)
            wx.BeginBusyCursor()
            self.image = wx.Image(filename, wx.BITMAP_TYPE_ANY, -1) # Load the image from the filename and auto-detect file type
            self.StatusBar.SetStatusText("Size = %s" %(str(self.image.GetSize())), 1) # Set status bar to show image's size
            self.ShowBitmap() # Display the image inside the panel
            wx.EndBusyCursor()

            dlg.Destroy() # Clean up dialog when its no longer needed

    def ShowBitmap(self):
            self.bitmap = wx.StaticBitmap(self.panel, -1, wx.BitmapFromImage(self.image)) # Convert to Bitmap to draw the image to the screen
            self.SetClientSize(self.bitmap.GetSize()) # Resize the application window to fit the image
            self.Center()
        

    def OnExit(self, event):
        "Close the application by Destroying the object"
        #print "OnExit called"
        self.Destroy()
        

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
