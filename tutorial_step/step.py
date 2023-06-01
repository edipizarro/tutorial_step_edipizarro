from apf.core.step import GenericStep
import logging

class TutorialStep(GenericStep):
    """TutorialStep Description

    Parameters
    ----------
    consumer : GenericConsumer
        Description of parameter `consumer`.
    **step_args : type
        Other args passed to step (DB connections, API requests, etc.)

    """
    def __init__(
        self,
        config: dict = {},
        level: int = logging.INFO,
        **step_args,
    ):
        super().__init__(config=config, level=level, **step_args)

    def execute(self, messages: list):
        ################################
        #   Here comes the Step Logic  #
        ################################
        for message in messages:
            self.logger.info(message["number"])
        return messages
