stepsResult = []
users = []

def join(user):
    if(len(users) == 1):
        users.append(user)
        return 'ready'
    if(len(users) >2):
        return 'full'
    users.append(user)
    return 'waiting'


def checkStepAvailable(step):
    stepsResult.append(step)
    return {"allSteps": stepsResult, "result": "ok"}