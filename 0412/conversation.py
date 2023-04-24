
def conversation(question):
    import viVoicecloud as vv
    from sjtu import analyze

    vv.Login()
    t = vv.tts()
    while 1:
        try:
            # question = input("I:")
            json_data = vv.aiui(question)
            # print(json_data)
            # print(type(json_data))

            answer = analyze.aiui_answer(json_data)
            print("R:" + answer)

            t.say(answer,voice="nannan")

        except Exception as e:
            print(e)
            vv.Logout()
            break

    vv.Logout()

