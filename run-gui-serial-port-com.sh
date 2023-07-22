#!/bin/bash

# Start a new tmux session in detached mode
tmux new-session -d -s my_session 

# Split the window vertically
tmux split-window -v

# Run 'ls' command in the left pane (pane 0)
tmux send-keys -t my_session:0.0 'cd gui-js; yarn electron:serve' C-m 

# Run 'top' command in the right pane (pane 1)
tmux send-keys -t my_session:0.1 'cd serial-port-communicator; python data-pipeline-gui-to-arduino.py' C-m 

# Attach to the created tmux session
tmux attach-session -t my_session
