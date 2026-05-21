# Q1. Modeling and Simulation of a Unicycle Robot
Tasks:
a) Derive the kinematic equations of a unicycle robot and explain the meaning of each
variable.
b) Explain the concept of the non-holonomic constraint and its physical significance.
c) Simulate the robot motion under the following conditions:
• Straight-line motion
• Pure rotational motion
• Circular motion
d) Plot the trajectory (X–Y plane) for each case and interpret the results.

# Q2. Design and Performance Analysis of PID Controller
Tasks:
a) Define proportional, integral, and derivative control actions and explain their individual
roles.
b) Develop a PID controller for a unicycle robot to move from an initial position to a desired
target position.
c) Implement and simulate the following controllers:
• P controller
• PI controller
• PD controller
• PID controller
d) For each case, plot:
• Robot trajectory
• Error versus time
e) Compare the performance in terms of:
• Convergence speed
• Overshoot
• Steady-state error
• Stability

# Q3. Linear Quadratic Regulator (LQR) Design
Tasks:
a) Explain the concept of LQR and formulate the cost function used in optimal control.
b) For a given linear system, derive the optimal control law and explain the role of matrices
(Q) and (R).
c) Analyze how varying (Q) and (R) affects system behavior (aggressiveness vs smoothness).
d) Compare LQR with PID control in terms of design approach, performance, and limitations.

# Q4. LQR-Based Control of a Unicycle System
Tasks:
a) Convert the nonlinear unicycle model into an error-state representation.
b) Linearize the system around an operating point.
c) Design an LQR controller by selecting appropriate (Q) and (R) matrices.
d) Simulate the robot motion from an initial position to a desired goal position.
e) Compare the results with PID control in terms of:
• Path smoothness
• Control effort
• Accuracy of convergence