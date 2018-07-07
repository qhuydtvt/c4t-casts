from renderers.animation import Animation

class PlayerAnimator:
    def __init__(self):
        self.left_animation = Animation(["images/player/player_left1.png",
                                         "images/player/player_left2.png",
                                         "images/player/player_left3.png",
                                         "images/player/player_left4.png",],
                                        loop=True)
        self.straight_animation = Animation(["images/player/player1.png",
                                             "images/player/player2.png",
                                             "images/player/player3.png",
                                             "images/player/player4.png",],
                                            loop=True)
        self.right_animation = Animation(["images/player/player_right1.png",
                                          "images/player/player_right2.png",
                                          "images/player/player_right3.png",
                                          "images/player/player_right4.png"],
                                         loop=True)

        self.current_animation = self.straight_animation

    def render(self, canvas, x, y):
        self.current_animation.render(canvas, x, y)

    def update(self, player_dx, player_dy):
        if player_dx < 0:
            self.current_animation = self.left_animation
        elif player_dx > 0:
            self.current_animation =  self.right_animation
        else:
            self.current_animation = self.straight_animation