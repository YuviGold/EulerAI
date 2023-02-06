function colorize(text, color) {
    if (ENVIRON["TERM"] == "xterm-color" || ENVIRON["TERM"] ~ /-256color$/) {
         return color text COLOR_OFF;
     } else {
         return text
     }
}

function help_category(title) {
    printf "\n%s\n", colorize(title, COLOR_BOLD);
}

function help_entry(target, desc) {
    printf "  %-20s %s\n", colorize(target, COLOR_CYAN), desc;
}

BEGIN {
    COLOR_OFF = "\033[0m"
    COLOR_BOLD = "\033[1m"
    COLOR_CYAN = "\033[36m"
    FS = ":.*##";
    printf "\nUsage:\n  make %s\n", colorize("<target>", COLOR_CYAN);
}

/^[a-zA-Z_0-9-]+:.*?##/ {
    help_entry($1, $2);
}

/^##@/ {
    help_category(substr($0, 5));
}

END {
    print "";
}
