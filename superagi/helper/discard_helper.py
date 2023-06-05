from superagi.tools.thinking.tools import LlmThinkingTool


def response(message) -> str:
    returnmsg = message.lower()
    if returnmsg != '' and returnmsg != None:
        if returnmsg[:1] == "?":
            obj_llm = LlmThinkingTool()
            return obj_llm._execute(returnmsg)

    #  return 'Yeah, I don\'t know. Try typing "!help".'