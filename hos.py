import urwid
import os


# Function to exit the application when 'q' is pressed
def exit_on_q(key):
    if key in ("q", "Q"):
        raise urwid.ExitMainLoop()


# Function to add a new hostname to the list
def add_host(new_host_edit, host_list_walker):
    new_host = new_host_edit.get_edit_text().strip()
    if new_host:
        host_list_walker.append(
            urwid.AttrMap(urwid.Text(new_host), None, focus_map="reversed")
        )
        new_host_edit.set_edit_text("")  # Clear the input after adding
        add_to_hosts(new_host)


# Function to add a domain to /etc/hosts
def add_to_hosts(domain):
    hosts_path = "/etc/hosts"
    entry = f"127.0.0.1 {domain}\n"
    try:
        with open(hosts_path, "a") as hosts_file:
            hosts_file.write(entry)
    except PermissionError:
        print(
            "Permission denied: Unable to write to /etc/hosts. Please run as root or with sudo."
        )


# Function to read existing hosts from /etc/hosts
def load_existing_hosts():
    hosts_path = "/etc/hosts"
    existing_hosts = []
    try:
        with open(hosts_path, "r") as hosts_file:
            lines = hosts_file.readlines()
            for line in lines:
                if line.startswith("127.0.0.1"):
                    domain = line.split()[1]
                    existing_hosts.append(domain)
    except PermissionError:
        print(
            "Permission denied: Unable to read /etc/hosts. Please run as root or with sudo."
        )
    return existing_hosts


# Function to delete a host from the list and from /etc/hosts
def delete_host(host_list_walker, listbox):
    if len(host_list_walker):
        focus_widget, focus_index = listbox.get_focus()
        domain = focus_widget.base_widget.get_text()[0]  # Extract the domain name
        del host_list_walker[focus_index]
        remove_from_hosts(domain)


# Function to remove a domain from /etc/hosts
def remove_from_hosts(domain):
    hosts_path = "/etc/hosts"
    try:
        with open(hosts_path, "r") as hosts_file:
            lines = hosts_file.readlines()
        with open(hosts_path, "w") as hosts_file:
            for line in lines:
                if domain not in line:
                    hosts_file.write(line)
    except PermissionError:
        print(
            "Permission denied: Unable to write to /etc/hosts. Please run as root or with sudo."
        )


# Main function to set up and run the UI
def main():
    global host_list  # Зробити змінну глобальною
    global host_list_walker  # Зробити змінну глобальною
    global loop  # Зробити змінну глобальною
    global new_host  # Зробити змінну глобальною

    # Create a text widget for the header, centered alignment
    header = urwid.Text("", align="center")

    # Create an edit widget for entering a new hostname
    new_host = urwid.Edit("add: ")

    # Create an instruction text
    instructions = urwid.Text(
        "\n".join(
            [
                "Instructions:",
                " - Press Q to exit",
                " - Tab to switch focus",
                " - Enter to add host",
                " - Delete to remove host",
            ]
        ),
        align="left",
    )

    # ASCII logo text
    LOGO_TEXT = """
                                   ___
 _______                  /__/
|.-----.|            ,---[___]*
||     ||           /    routrer
||_____||    _____ /        ____
|o_____*|   [o_+_+]--------[=i==]
 |     ________| 850        drive
 |  __|_        interface
 '-/_==_\\
  /_____\\  ATARI 800       -nesnite-
       """

    # ASCII logo widget
    ascii_logo = urwid.Text(("logo", LOGO_TEXT), align="left")

    # Create a vertical pile for the left section (edit field + instructions + logo)
    left_pile = urwid.Pile(
        [
            urwid.Padding(new_host, left=1, right=1),
            urwid.Divider(),  # Add a space between the input field and instructions
            urwid.Padding(instructions, left=1, right=1),
            urwid.Divider(),  # Add a space between instructions and the logo
            urwid.Padding(ascii_logo, left=1, right=1),
        ]
    )

    # Wrap the left pile in a BoxAdapter to control its size
    new_host_box = urwid.BoxAdapter(urwid.Filler(left_pile, valign="top"), height=18)

    # Create a listbox for displaying the list of created hosts
    host_list_walker = urwid.SimpleFocusListWalker([])

    # Load existing hosts from /etc/hosts
    existing_hosts = load_existing_hosts()
    for host in existing_hosts:
        host_list_walker.append(
            urwid.AttrMap(urwid.Text(host), None, focus_map="reversed")
        )

    host_list = urwid.ListBox(host_list_walker)

    # Add padding to the host list to create space from the main border
    padded_host_list = urwid.Padding(host_list, left=1, right=1)

    # Create a line box for the list of hosts
    host_list_box = urwid.LineBox(padded_host_list, title="List of hosts names")

    # Add padding to the columns to create space from the main border
    columns = urwid.Columns(
        [("weight", 1, new_host_box), ("weight", 1, host_list_box)],
        dividechars=1,
    )
    columns_padded = urwid.Padding(columns, left=2, right=2)

    # Create a text widget for the footer with an empty text for the bottom padding
    footer = urwid.Text("", align="center")

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
        palette=[
            ("linebox", "light cyan", "black"),
            ("reversed", "standout", ""),
            ("logo", "light cyan", "black"),
        ],
        unhandled_input=exit_on_q,
    )

    # Handle input for switching focus, adding hosts, deleting hosts, and exiting
    loop.unhandled_input = handle_input
    loop.run()


def handle_input(key):
    global host_list  # Використати глобальні змінні
    global host_list_walker  # Використати глобальні змінні
    global new_host  # Використати глобальні змінні

    if key == "tab":
        focus_position = columns.get_focus_column()
        if focus_position == 0:
            columns.set_focus_column(1)
        else:
            columns.set_focus_column(0)
    elif key == "enter":
        add_host(new_host, host_list_walker)
    elif key == "q":
        raise urwid.ExitMainLoop()
    elif key in ("delete", "d"):
        delete_host(host_list_walker, host_list)
    elif key == "up":
        if host_list.focus_position > 0:
            host_list.focus_position -= 1
    elif key == "down":
        if host_list.focus_position < len(host_list_walker) - 1:
            host_list.focus_position += 1


# Check if this script is being run directly
if __name__ == "__main__":
    main()
