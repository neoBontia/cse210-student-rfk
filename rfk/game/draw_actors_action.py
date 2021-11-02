from game.action import Action

class DrawActorsAction(Action):
    def __init__(self, output_service):
        self._outputService = output_service

    def execute(self, cast):
        self._outputService.clear_screen()
        
        marquee = cast["marquee"][0]
        self._outputService.draw_actor(marquee)
        robot = cast["robot"][0]
        self._outputService.draw_actor(robot)
        artifacts = cast["artifact"]
        self._outputService.draw_actors(artifacts)

        self._outputService.flush_buffer()
