from typing import Dict


class Task:
    """task invoking base class,all the task should be extended to this class
        and override this method"""
    def invoke(self, data: Dict) -> Dict:
        """
        invoke:
        
        paras:
            data: receive JSON data
            
        return:
            JSON response
        """
        raise NotImplementedError("Warning: the method invoke of the class Task must be override")