# Python Terminal-Based Brick-Breaking game

## How to run the game
`python3 game.py`

## Controls
- q -> to quit game
- s -> to release the ball from paddle
- a -> to move paddle to left
- d -> to move paddle to right
- l -> to change the level

## Rules and Functionality
- Score ,Lives, Levels and Time played is displayed on screen .
- There are **3 levels** where you can go to next level by pressing `l`.
-- First two levels are normal one but the third level is boss level consisting of an **enemy `UFO`**, it will move along with the paddle but be save , it can throw bombs on you :{  . Initially bomb has power of 5 that means ball needs to hit it 5 times to kill it . Moreover it has some alien powers also , when its health is decreased to 3 or 1 , it can protect itself by forming a defensive brick layer. its health will also be shown on screen. You can get 20 points each time you hit the enemy and can get 100 points if the enemy is destroyed completely.
- There are **6 types of brick** 
-- Green colored brick which have strength 1 
-- Yellow colored brick which have strength 2
-- Blue colored brick which have strength 3
-- Magenta colored brick which are unbreakable (considering it of strength 4 if it breaks)
-- Red colored brick are the exploding bricks (considering it of strength 1)
-- **Rainbow bricks** are those bricks continuously changing their color and        strength (1->4) , when ball collides with this brick ,brick changing will stop and it will become the    type of brick it was at the time of collision.
- Whenever strength of brick is reduced , he will get 10*strength_reduced points in score, For eg if yellow brick is hit by ball then he get 10 points and yellow brick is changed into green brick .but if ball has a powerup or yellow ball is nearby the exploding brick , he will get 20 points. and yellow brick will get disappear.
- when exploding brick is hit ,all bricks adjacent are also destroyed.
- Ball also suffers **collision of three types** 
-- with wall , perpendicular direction velocity is reversed.
-- with paddle , velocity in direction of paddle is increased or decreased with respect to distance from centre of paddle.
-- with bricks , velocity is changed with respect to the point on which ball hits the brick
- **Falling bricks** - the whole layout will shift downward with 1 unit after reaching a certain time when ball hits the paddle . if the lowest brick reaches the paddle level , the game is over :{
-- *Cheat for this is press `l` whenever you feel you cant get more points from this level.:}*
- **Powerups** . all will be availabe for 10 units if paddle catch the powerup, if he get two same powerup at a time the time for that powerup is increased only. and if two different powerups he got , they both will act simultaneously.
-- Expand paddle - Length of paddle is increased by 2 units
-- Shrink paddle - Length of paddle is decreased by 2 units
-- Fast ball - speed of ball is increased
-- Thru ball - ball can destroy any brick it touches irrespective of strength and move through the bricks without any collision taking place .
-- Paddle grab - each time paddle recieves the ball, it will stick onto the paddle and user need to press `s` to move ball from paddle.
-- **Shooting paddle** - paddle will get two guns which will shoot bullets after some time , these bullets when hit the brick it will act as ball and disappear after hitting the bricks.
-- **Fire ball** - Each time ball hit the brick , all bricks nearby it irrespective of its strength will be vanished.
- **Powerup 2.0** isimplemented for fireball and shooting paddle powerup , instead of powerup droping down it will recieve the velocity of ball and move with that and will experience gravity also. Collision of these powerup with wall is similar to that of ball. 
- To increase the user experience , there are **sound effects** also for ball hitting the paddle, brick or wall; exploding bricks; shooting lasers; boss enemy music; losing life.
- The code follow OOPs concepts

Be patient with the game , it lags a lot :( 