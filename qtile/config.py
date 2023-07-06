import logging
import os
import subprocess

from libqtile import bar, hook, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.layout.columns import Columns
from libqtile.layout.floating import Floating
from libqtile.lazy import lazy

mod = "mod4"

logger = logging.getLogger("qtile.config")

keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key(
        [mod, "shift"],
        "Left",
        lazy.layout.shuffle_left(),
        desc="Move window to the left",
    ),
    Key(
        [mod, "shift"],
        "Right",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    Key(
        [mod, "control"],
        "Left",
        lazy.layout.grow_left(),
        desc="Grow window to the left",
    ),
    Key(
        [mod, "control"],
        "Right",
        lazy.layout.grow_right(),
        desc="Grow window to the right",
    ),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn("kitty"), desc="Launch terminal"),
    Key([mod], "space", lazy.spawn("rofi -show drun"), desc="Launch rofi drun menu."),
    Key(
        [mod],
        "Tab",
        lazy.window.toggle_floating(),
        # lazy.next_layout(),
        desc="Toggle between floating and tiling layout.",
    ),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod, "shift"], "s", lazy.spawn("/home/akai/.flameshot-tixte/screenshot.sh")),
]


groups = [Group(str(i + 1), label="") for i in range(8)]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )


layouts = [
    Columns(
        margin=10,
        border_width=2,
        border_focus="#4abaaf",
        border_normal="#4e5173",
        border_on_single=True,
    ),
]

# From cozytile.


def search():
    qtile.cmd_spawn("rofi -show drun")


def power():
    command = os.path.expanduser("~/.config/rofi/scripts/powermenu/powermenu.sh")
    subprocess.call([command])


top_bar = bar.Bar(
    [
        widget.Spacer(
            length=15,
            background="#282738",
        ),
        widget.Image(
            filename="~/.config/qtile/assets/shutdown.png",
            margin=2,
            background="#282738",
            mouse_callbacks={"Button1": power},
        ),
        widget.Image(
            filename="~/.config/qtile/assets/6.png",
        ),
        widget.GroupBox(
            font="JetBrains Mono Nerd Font",
            fontsize=18,
            borderwidth=3,
            highlight_method="block",
            active="#4abaaf",
            block_highlight_text_color="#8eddd7",
            highlight_color="#4B427E",
            inactive="#282738",
            foreground="#4B427E",
            background="#353446",
            this_current_screen_border="#353446",
            this_screen_border="#353446",
            other_current_screen_border="#353446",
            other_screen_border="#353446",
            urgent_border="#353446",
            rounded=True,
            disable_drag=True,
        ),
        widget.Image(
            filename="~/.config/qtile/assets/5.png",
        ),
        widget.Image(
            filename="~/.config/qtile/assets/search.png",
            margin=2,
            background="#282738",
            mouse_callbacks={"Button1": search},
        ),
        widget.TextBox(
            fmt="Search",
            background="#282738",
            font="JetBrains Mono Bold",
            fontsize=15,
            foreground="#4abaaf",
            mouse_callbacks={"Button1": search},
        ),
        widget.Image(
            filename="~/.config/qtile/assets/4.png",
        ),
        widget.Spacer(length=455, background="#353446"),
        widget.Image(
            filename="~/.config/qtile/assets/3.png",
        ),
        widget.Image(
            filename="~/.config/qtile/assets/wifi.png",
        ),
        widget.Wlan(
            background="#282738",
            font="JetBrains Mono Bold",
            fontsize=13,
            foreground="#4abaaf",
            interface="wlx00e02d84276c",
            update_interval=5,
            format="{essid}",
        ),
        widget.Image(
            filename="~/.config/qtile/assets/6.png",
            background="#353446",
        ),
        widget.Image(
            filename="~/.config/qtile/assets/Misc/ram.png",
            background="#353446",
        ),
        widget.Memory(
            background="#353446",
            format="{MemUsed: .0f}{mm}",
            foreground="#4abaaf",
            font="JetBrains Mono Bold",
            fontsize=13,
            update_interval=5,
        ),
        widget.Image(
            filename="~/.config/qtile/assets/2.png",
        ),
        widget.Spacer(
            length=8,
            background="#353446",
        ),
        widget.Volume(
            font="JetBrains Mono Bold",
            fontsize=13,
            theme_path="~/.config/qtile/assets/Volume/",
            emoji=True,
            background="#353446",
        ),
        widget.Volume(
            font="JetBrains Mono Bold",
            fontsize=13,
            background="#353446",
            foreground="#4abaaf",
        ),
        widget.Image(
            filename="~/.config/qtile/assets/5.png",
            background="#353446",
        ),
        widget.Image(
            filename="~/.config/qtile/assets/Misc/clock.png",
            background="#282738",
            margin_y=6,
            margin_x=5,
        ),
        widget.Clock(
            format="%I:%M %p",
            background="#282738",
            foreground="#4abaaf",
            font="JetBrains Mono Bold",
            fontsize=13,
        ),
        widget.Spacer(
            length=18,
            background="#282738",
        ),
    ],
    30,
    background="#282738",
    border_color="#282738",
    border_width=[0, 0, 0, 0],
    margin=[8, 10, 0, 10],
)

screens = [
    Screen(
        top=top_bar,
        wallpaper="~/.config/qtile/assets/wallpaper.png",
        wallpaper_mode="fill",
    )
]


mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = Floating(
    border_width=2,
    border_focus="#4abaaf",
    border_normal="#4e5173",
    float_rules=[
        *Floating.default_float_rules,
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry"),
    ],
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True


auto_minimize = True


wl_input_rules = None


wmname = "LG3D"


@hook.subscribe.startup_once
def autostart():
    command = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.call([command])
    top_bar.window.window.set_property("QTILE_BAR", 1, "CARDINAL", 32)  # type: ignore
