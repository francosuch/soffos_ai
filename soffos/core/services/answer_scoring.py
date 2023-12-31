'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-04-18
Purpose: Handler of Answer Scoring Service
-----------------------------------------------------
'''
from .service import SoffosAIService
from soffos.common.constants import ServiceString

class AnswerScoringService(SoffosAIService):
    '''
    For service description please go to:
    https://dev-platform.soffos.ai/playground/docs#/answer-scoring
    '''

    def __init__(self, apikey, user, src=None, concern=None, **kwargs) -> None:
        super().__init__(apikey, user, src, concern)
        self._service = ServiceString.ANSWER_SCORING
        

    def allow_input(self, source, concern):

        if not isinstance(source, self.provide_source_type()):
            return False, "Please provide a dictionary on your source <src>"
        
        if not concern:
            if "user_answer" in source.keys():
                self._concern = source['user_answer']
                concern = self._concern
            else:
                return False, "Please provide user_answer"

        if not isinstance(concern, str):
            return False, "Please provide a string datatype for user_answer"
        
        if "context" not in source.keys():
            return False, "Please provide context key on your source <src> dictionary."
        
        if "question" not in source.keys():
            return False, "Please provide question key on your source <src> dictionary."
        
        if "answer" not in source.keys():
            return False, "Please provide answer key on your source <src> dictionary."
        
        return True, None

    def provide_output_type(self):
        return float
    
    def provide_source_type(self):
        return dict
    
    def provide_concern_type(self):
        return str
    
    def get_default_output_key(self):
        return "score"
    
    def get_default_secondary_output_key(self):
        return None

    def get_json(self):
        request_data = {
            "user": self._user,
            "context": self._src['context'],
            "question": self._src['question'],
            "answer": self._src['answer'],
            "user_answer": self._concern
        }

        return request_data
