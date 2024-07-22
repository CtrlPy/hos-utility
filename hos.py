import urwid


# Function to exit the application when 'q' is pressed
def exit_on_q(key):
    if key in ("q", "Q"):
        raise urwid.ExitMainLoop()


# Main function to set up and run the UI
def main():
    # Create a text widget for the header, centered alignment
    header = urwid.Text("", align="center")

    # Create an edit widget for entering a new hostname
    new_host = urwid.Edit("add: ")

    # Wrap the edit widget in a BoxAdapter to control its size
    new_host_box = urwid.BoxAdapter(urwid.Filler(new_host, valign="top"), height=1)

    # Add padding to the new host box to create internal margins
    new_host_padded = urwid.Padding(new_host_box, left=1, right=1)

    # Create a listbox for displaying the list of created hosts
    host_list = urwid.ListBox(
        urwid.SimpleFocusListWalker(
            [
                urwid.Padding(urwid.Text("Hostname 1"), left=2),
                urwid.Padding(urwid.Text("Hostname 2"), left=2),
                urwid.Padding(urwid.Text("Hostname 3"), left=2),
            ]
        )
    )

    # Create a line box for the new host input
    new_host_linebox = urwid.LineBox(new_host_padded, title="new host")

    # Create a line box for the list of hosts
    host_list_box = urwid.LineBox(host_list, title="List of hosts names")

    # Add padding to the columns to create space from the main border
    columns_padded = urwid.Padding(
        urwid.Columns(
            [("weight", 1, new_host_linebox), ("weight", 1, host_list_box)],
            dividechars=1,
        ),
        left=2,
        right=2,
    )

    # Create a text widget for the footer, centered alignment
    footer = urwid.Text("Press Q to exit", align="center")

    # Add padding to the footer to create space from the main border
    footer_padded = urwid.Padding(footer, left=2, right=2)

    # Create a frame with the header, body, and footer
    frame = urwid.Frame(header=header, body=columns_padded, footer=footer_padded)

    # Create a line box around the frame to create a border
    bordered_frame = urwid.LineBox(
        frame,
        title="hos",
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
