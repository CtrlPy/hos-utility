import urwid


# Function to exit the application when 'q' is pressed
def exit_on_q(key):
    if key in ("q", "Q"):
        raise urwid.ExitMainLoop()


# Main function to set up and run the UI
def main():
    # Create a text widget for the header, centered alignment
    header = urwid.Text("Logo and Name Utility", align="center")

    # Create an edit widget for entering a new hostname
    new_host = urwid.Edit("Add a new hostname: ")

    # Create a listbox for displaying the list of created hosts
    host_list = urwid.ListBox(
        urwid.SimpleFocusListWalker(
            [
                urwid.Text("Hostname 1"),
                urwid.Text("Hostname 2"),
                urwid.Text("Hostname 3"),
            ]
        )
    )

    # Create a line box for the new host input
    new_host_box = urwid.LineBox(urwid.Pile([new_host]), title="Add a new hostname")

    # Create a line box for the list of hosts
    host_list_box = urwid.LineBox(host_list, title="List of domain names")

    # Combine the columns into a single widget
    columns = urwid.Columns(
        [("weight", 1, new_host_box), ("weight", 1, host_list_box)], dividechars=1
    )

    # Create a text widget for the footer, centered alignment
    footer = urwid.Text("Press Q to exit", align="center")

    # Create a frame with the header, body, and footer
    frame = urwid.Frame(header=header, body=columns, footer=footer)

    # Create a line box around the frame to create a border
    bordered_frame = urwid.LineBox(
        frame,
        title="hos utility",
        tlcorner="┌",
        tline="─",
        lline="│",
        rline="│",
        blcorner="└",
        bline="─",
        trcorner="┐",
        brcorner="┘",
    )

    # Apply the color attribute to the bordered_frame
    colored_frame = urwid.AttrMap(bordered_frame, "linebox")

    # Create and run the main event loop
    loop = urwid.MainLoop(
        colored_frame,
        palette=[("linebox", "light cyan", "black")],
        unhandled_input=exit_on_q,
    )
    loop.run()


# Check if this script is being run directly
if __name__ == "__main__":
    main()
