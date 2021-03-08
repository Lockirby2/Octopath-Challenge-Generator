import Config

class Restriction(object):
    def initialize(self, name, maxInvocations, weight, chapters, conflictsWith=[]): # Initialize the restriction
        self.name = name # Identifies the restriction for use in determining conflicts
        self.maxInvocations = maxInvocations # The maximum number of times the restriction can be applied
        self.weight = weight # If the weight is higher, the restriction is more likely to be applied
        self.chapters = chapters # The chapters in which this restriction can be applied
        self.conflictsWith = conflictsWith # The restrictions that this restriction conflicts with
        self.invocations = 0
       
    def conflicts(self, restrictions): # Determines if the restriction can be applied
        if not Config.chapter in self.chapters: return True
        if self.invocations >= self.maxInvocations: return True
        for conflictName in self.conflictsWith:
            if any(r.name == conflictName and r.invocations >= 1 for r in restrictions):
                return True
        return False
       
    def invoke(self): # This method should do all the work necessary to apply the restriction
        self.invocations += 1
        
    def output(self): # This method should print the description of the restriction to the user
        pass