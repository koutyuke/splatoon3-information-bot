from module.info.getInfo import getInfo
from module.info.TimeData import createTimeData


def getSchedule(token: str) -> object:
    sha256hash = "7d4bb0565342b7385ceb97d109e14897"
    postResponse = getInfo(token=token, sha256Hash=sha256hash)

    if postResponse[0] in range(200, 300):
        postResponse = postResponse[1]["data"]
    else:
        return "error"

    responseRegular = postResponse["regularSchedules"]["nodes"]
    # p(responseRegular)
    responseBankara = postResponse["bankaraSchedules"]["nodes"]
    responseX = postResponse["xSchedules"]["nodes"]
    responseLeague = postResponse["leagueSchedules"]["nodes"]

    regularDataArr = []
    challengeDataArr = []
    openDataArr = []
    XDataArr = []
    leagueDataArr = []

    for i in range(3):
        type = "now" if i == 0 else "next" if i == 1 else "nextnext"

        regularData = responseRegular[i]
        bankaraData = responseBankara[i]
        XData = responseX[i]
        leagueData = responseLeague[i]

        challengeData = (
            bankaraData["bankaraMatchSettings"][0]
            if bankaraData["bankaraMatchSettings"][0] == "CHALLENGE"
            else bankaraData["bankaraMatchSettings"][1]
        )
        openData = (
            bankaraData["bankaraMatchSettings"][0]
            if bankaraData["bankaraMatchSettings"][0] == "OPEN"
            else bankaraData["bankaraMatchSettings"][1]
        )

        regularTime = createTimeData(regularData["startTime"], regularData["endTime"])
        bankaraTime = createTimeData(bankaraData["startTime"], bankaraData["endTime"])
        XTime = createTimeData(XData["startTime"], XData["endTime"])
        leagueTime = createTimeData(leagueData["startTime"], leagueData["endTime"])

        if not regularData["festMatchSetting"] == None:
            regularDataArr.append(
                {
                    "type": type,
                    "rule": None,
                    "time": None,
                    "stage": None,
                    "isFest": True,
                }
            )

        else:
            stage = [
                stages["name"]
                for stages in regularData["regularMatchSetting"]["vsStages"]
            ]
            rule = regularData["regularMatchSetting"]["vsRule"]["name"]
            regularDataArr.append(
                {
                    "type": type,
                    "rule": rule,
                    "time": regularTime,
                    "stage": stage,
                    "isFest": False,
                }
            )

        if not bankaraData["festMatchSetting"] == None:
            openDataArr.append(
                {
                    "type": type,
                    "rule": None,
                    "time": None,
                    "stage": None,
                    "isFest": True,
                }
            )

            challengeDataArr.append(
                {
                    "type": type,
                    "rule": None,
                    "time": None,
                    "stage": None,
                    "isFest": True,
                }
            )
        else:
            openStage = [stages["name"] for stages in openData["vsStages"]]
            challengeStage = [stages["name"] for stages in challengeData["vsStages"]]

            openRule = openData["vsRule"]["name"]
            challengeRule = challengeData["vsRule"]["name"]

            openDataArr.append(
                {
                    "type": type,
                    "rule": openRule,
                    "time": bankaraTime,
                    "stage": openStage,
                    "isFest": False,
                }
            )

            challengeDataArr.append(
                {
                    "type": type,
                    "rule": challengeRule,
                    "time": bankaraTime,
                    "stage": challengeStage,
                    "isFest": False,
                }
            )

        if not XData["festMatchSetting"] == None:
            XDataArr.append(
                {
                    "type": type,
                    "rule": None,
                    "time": None,
                    "stage": None,
                    "isFest": True,
                }
            )

        else:
            stage = [stages["name"] for stages in XData["xMatchSetting"]["vsStages"]]
            rule = XData["xMatchSetting"]["vsRule"]["name"]
            XDataArr.append(
                {
                    "type": type,
                    "rule": rule,
                    "time": XTime,
                    "stage": stage,
                    "isFest": False,
                }
            )

        if not leagueData["festMatchSetting"] == None:
            leagueDataArr.append(
                {
                    "type": type,
                    "rule": None,
                    "time": None,
                    "stage": None,
                    "isFest": True,
                }
            )

        else:
            stage = [
                stages["name"]
                for stages in leagueData["leagueMatchSetting"]["vsStages"]
            ]
            rule = leagueData["leagueMatchSetting"]["vsRule"]["name"]
            leagueDataArr.append(
                {
                    "type": type,
                    "rule": rule,
                    "time": leagueTime,
                    "stage": stage,
                    "isFest": False,
                }
            )

    return {
        "regular": regularDataArr,
        "charenge": challengeDataArr,
        "open": openDataArr,
        "x": XDataArr,
        "league": leagueDataArr,
    }
