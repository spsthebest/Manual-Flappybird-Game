# flappybird
Flappybird Game Python
About the code:

1. General Understanding
Primary components of the game : 
  A. Birds
  B. Pipes
  C. Scoring System

2. How does the bird’s movement work? The bird moves based on gravity and jumping mechanism. 

3. How are the pipes generated and managed? Pipes are generated with random height and move leftwards. When they move off the screen, they are resetted to the right edge with a new height.

4. Code Functionality: bird_y_change represents the vertical speed of the bird. It starts at 0 and is updated by adding the gravity in each frame. Its set to jump when the spacebar is pressed

5. How does the collision detection work? The code checks if the bird hits the top or bottom of the screen or collides with the pipe by comparing the bird’s position with the pipe’s position. 

6. show_score() : This function displays the current score at the top left corner of the screen. The game checks if the bird is out of bound or collides with the pipe to set game_over.

7. Enhancement: How can the graphics and user experience be improved? Consider adding images for the bird and pipes instead of simple rectangles and add sound effects and animation for  better ux.

8. How can the game mechanics be refined? Adjust gravity, jump height and pipe speed to fine tune the gameplay difficulty. Implementing better collision detection and physics can improve game feel. 

9. How can AI be integrated into the game? Implement basic AI or ML algorithms to control the bird automatically, making decisions based on the pipe position and gaps.

10. UI and experience: Improve the display of the score, game over message and other text elements for better visibility.
