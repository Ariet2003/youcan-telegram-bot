from aiogram import Router

router = Router()

# # Dictionary for storing message IDs
# sent_message_add_screen_ids = {
#     'bot_messages': [],
#     'user_messages': []
# }
# Dictionary for storing message IDs per user
sent_message_add_screen_ids = {}

pictureOfUsersPersonalAccountKG = 'AgACAgIAAxkBAAIBgWchCkcUvNa6ujUOz3H_XzLoNs6_AALV5TEb7pMISalMM-81H-LZAQADAgADeQADNgQ'
pictureOfUsersPersonalAccountRU = 'AgACAgIAAxkBAAIBnGch3tJHJyBPCATGYyoTadR2-RbxAALE5jEbbWgJSUSeqRMgQl2TAQADAgADeQADNgQ'
subjectSelectionKG = 'AgACAgIAAxkBAAICpGcke6EdIaK01XtNv5XJOdrfEHu6AAKJ4DEbNSQoSd1QW5k0_RXHAQADAgADeQADNgQ'
subjectSelectionRU = 'AgACAgIAAxkBAAICqGckfCzO1XF2Q6zsZZmnDBDluNLlAAKN4DEbNSQoSXcHg02yrumdAQADAgADeQADNgQ'
pictureForTheTestCreationScreenKG = 'AgACAgIAAxkBAAIFSWcmHyUFKrpTky_q-KCN8Z6dO6bhAAL-6TEbofYxSVcdNZnyXG9hAQADAgADeQADNgQ'
pictureForTheTestCreationScreenRU = 'AgACAgIAAxkBAAIFTWcmH3iby3brbhYdrFN0EJHRaCKiAAL_6TEbofYxSaBlhn8q_H1CAQADAgADeQADNgQ'
pictureForTheEditAnAnalogyKG = 'AgACAgIAAxkBAAIFXWcmIEtD84qRlzDMl6YeU1yJY75oAAIE6jEbofYxSd_5Y2kuPr6AAQADAgADeQADNgQ'
pictureForTheEditAnAnalogyRU = 'AgACAgIAAxkBAAIFXWcmIEtD84qRlzDMl6YeU1yJY75oAAIE6jEbofYxSd_5Y2kuPr6AAQADAgADeQADNgQ'
pictureForTheEditAnGrammerKG = 'AgACAgIAAxkBAAIFc2cmISbDHpT7z50_AgsRXRW_pw7wAAIK6jEbofYxSYwquz6v_manAQADAgADeQADNgQ'
pictureForTheEditAnGrammerRU = 'AgACAgIAAxkBAAIFc2cmISbDHpT7z50_AgsRXRW_pw7wAAIK6jEbofYxSYwquz6v_manAQADAgADeQADNgQ'
picturePlusFiveRubin = 'AgACAgIAAxkBAAIIqmcrvDqWao3ogO-IYM-FMQkM80s7AAIF5DEb0ZBZSSl6H_4didP5AQADAgADeQADNgQ'
pictureBadRequests = 'AgACAgIAAxkBAAIJY2csV-BfGqRbaS87jUtdmVw-zMmPAAJt5DEbZE5oSRws4MdP8uDRAQADAgADeQADNgQ'
pictureOfAdminPersonalAccount = 'AgACAgIAAxkBAAIKHWcsbm18OBK0aTu2qyCSar53VdAnAAL95DEbZE5oSRCflZnKw3e5AQADAgADeQADNgQ'
pictureForValidationQuestions = 'AgACAgIAAxkBAAIKKWcseCNaZhvZYCi-_yV8x0jQlYXNAAJG5TEbZE5oSXpzWxeG6OnPAQADAgADeQADNgQ'
pictureForAddUserVIP = 'AgACAgIAAxkBAAIK7mcsvZTFgLOD-G9OcxibMGVSAAFrgwACcecxG2ROaEngLr_3cda23AEAAwIAA3kAAzYE'
pictureSuccessProces = 'AgACAgIAAxkBAAIK8mcswd0KyhiSnAg4gjq9JiJ47YpKAAKh5zEbZE5oSSuS_FjorASQAQADAgADeQADNgQ'
pictureErrorProcess = 'AgACAgIAAxkBAAIK9mcswgK_YPTK5xtzX37LahGRFppVAAKj5zEbZE5oSY8pmWUbP3wSAQADAgADeQADNgQ'
pictureForNotification = 'AgACAgIAAxkBAAILIWcs0WgUH_Q7V_7TqYIDtvKK4h5sAAJb6DEbZE5oSUuSKEqMORNkAQADAgADeQADNgQ'
pictureForStatistics = 'AgACAgIAAxkBAAIL5Wcs8ueR_6ezAoUNMQ8VkPJ6iUqTAAJ56TEbZE5oSUBJSyy69-PBAQADAgADeQADNgQ'
pictureForListUsers = 'AgACAgIAAxkBAAIMhGct5cwwPsw0kbOddXh1VKW_NK04AAJn6DEbqWBwSXSWL8B0RzxiAQADAgADeQADNgQ'
pictureForAdminSetting = 'AgACAgIAAxkBAAIM2WcvA4VyQWcmcGuH4nid-3qVcpJZAAKS4jEbqWB4SYCtUSko8h1TAQADAgADeQADNgQ'
PictureResetAllVipStatuses = 'AgACAgIAAxkBAAIM4WcvCVsKulzfR1J7gUKN31TH2PgKAAKw4jEbqWB4SURAFae9YUvJAQADAgADeQADNgQ'
pictureResetVipStatus = 'AgACAgIAAxkBAAINJGcvGcwVFd3Ta41o3PIUBZZFs-bVAAIO4zEbqWB4SVJHUr449SpQAQADAgADeQADNgQ'
pictureForGoToVIPKG = 'AgACAgIAAxkBAAINp2cvY5-JN92SI9YLVR2hxUHJv5_LAAJ-6DEbWH94ScFHzXM4HQ28AQADAgADeQADNgQ'
pictureForGoToVIPRU = 'AgACAgIAAxkBAAINq2cvY9W2wLbW3SbrTF7FqAhNuZAGAAJ_6DEbWH94STdnKTRigq7-AQADAgADeQADNgQ'
PictureForUserSettingsRU = 'AgACAgIAAxkBAAINuGcvkw5mN3VQWKieQ85sHnRuyieFAAI15jEbWH-ASW7o_IaYFxAqAQADAgADeQADNgQ'
PictureForUserSettingsKG = 'AgACAgIAAxkBAAINvGcvk4nCDSFEDzYHz4xOEPeLz0m-AAI85jEbWH-ASUtoI2zYV0BXAQADAgADeQADNgQ'
PictureForChangeLanguaageKG = 'AgACAgIAAxkBAAINzGcvmF4Ukh8zwq0JbnOgFx4GAnFuAAKK5jEbWH-ASf982wABVEoyGQEAAwIAA3kAAzYE'
PictureForChangeLanguaageRU = 'AgACAgIAAxkBAAIN0GcvmGehKMbLU4Ro7uQDwvy_1lhHAAKL5jEbWH-ASU3D0NUOLZN-AQADAgADeQADNgQ'
PictureForChangePhoneNumberRU = 'AgACAgIAAxkBAAIOBWcvoo-coauYxYb7j6WJvDGNKjoQAAPnMRtYf4BJf0SQjB-uJNoBAAMCAAN5AAM2BA'
PictureForChangePhoneNumberKG = 'AgACAgIAAxkBAAIOCWcvop0LOUbW1bSktbHPthFQkqPWAAIB5zEbWH-AScYyey8S8e1oAQADAgADeQADNgQ'
PictureForMyStatusRU = 'AgACAgIAAxkBAAIOK2cvpnpjbcOUVERnUMsDoTZlQhN0AAIW5zEbWH-ASVWaqpBKNl41AQADAgADeQADNgQ'
PictureForMyStatusKG = 'AgACAgIAAxkBAAIOL2cvppk0GgdhU2t361CquzY7ezebAAIX5zEbWH-ASQ5uzQLLgGJcAQADAgADeQADNgQ'
PictureForFAQKG = 'AgACAgIAAxkBAAIOaWcvrljru4iyvjLdmGxmZpgRVFVfAAJB5zEbWH-ASecG9UyaBCexAQADAgADeQADNgQ'
PictureForFAQRU = 'AgACAgIAAxkBAAIObWcvrmPTvtaTIhDd_lm5ubrJUFUjAAJC5zEbWH-ASRe_I-adcR7fAQADAgADeQADNgQ'
PictureForChangeNicknameRU = 'AgACAgIAAxkBAAIOf2cvsphNFGZOlnM7j5HbRKKjPjpKAAJe5zEbWH-ASfKqKyv6DC3OAQADAgADeQADNgQ'
PictureForChangeNicknameKG = 'AgACAgIAAxkBAAIOg2cvsqHENSUooWdtjtfIoJyvU84FAAJf5zEbWH-ASdMDzRXN5X9BAQADAgADeQADNgQ'
PictureForTakeTheTestKG = 'AgACAgIAAxkBAAIPUWcwzfV-EqusINtPULY_nBfcRelTAAID5zEbWH-ISSJUuEUoH3HuAQADAgADeQADNgQ'
PictureForTakeTheTestRU = 'AgACAgIAAxkBAAIPVWcwzf_AIYkSkr3-Bj-72TyuH0VaAAIE5zEbWH-ISZwOUrRsmiSsAQADAgADeQADNgQ'
PictureForTakeAnalogyQuestionRU = 'AgACAgIAAxkBAAIPsmcw9y02JLiv6M1nSE-4ujU6ecpTAAKI6DEbWH-ISSI-z2DcWn0TAQADAgADeQADNgQ'
PictureForTakeAnalogyQuestionKG = 'AgACAgIAAxkBAAIPsmcw9y02JLiv6M1nSE-4ujU6ecpTAAKI6DEbWH-ISSI-z2DcWn0TAQADAgADeQADNgQ'
PictureForTakeGrammarQuestionRU = 'AgACAgIAAxkBAAIQoGcxtMgIsPC_bEqdDoAAAawzq7JTcwACeeIxGzfRkEnTxae9Y1ktkQEAAwIAA3kAAzYE'
PictureForTakeGrammarQuestionKG = 'AgACAgIAAxkBAAIQoGcxtMgIsPC_bEqdDoAAAawzq7JTcwACeeIxGzfRkEnTxae9Y1ktkQEAAwIAA3kAAzYE'
PictureForCorrectAnswer = 'AgACAgIAAxkBAAIQAWcxAXYqWDLZRCVitKlmMP3pZqxeAALR6DEbWH-IScn9kiFh6amSAQADAgADeQADNgQ'
PictureForWrongAnswer = 'AgACAgIAAxkBAAIQBWcxAYe9TSlmXT6I-u62Cdh8lAgxAALS6DEbWH-ISQs6WKXnDxtmAQADAgADeQADNgQ'
PictureForDuel = 'AgACAgIAAxkBAAITsWc0tm5T7VGbJdiCoI2F7VQV5A_LAALY8zEb1t-gSXg3pHvzSqu_AQADAgADeQADNgQ'

PhoneNumberAdmin = '+996702160703'

PromptForChatGPTForKyrgyzAnalogyQuestion = ("Төмөндө берилген сөздөрдүн ортосундагы мамиле аналогиялык негизде түзүлгөн. "
                                            "Берилген жуптагы биринчи сөз менен экинчи сөз ортосунда кандай мамиле "
                                            "болсо, жооптордогу жуптардын биринде да ошондой байланыш болушу керек. "
                                            "Суроону жана жоопторду анализдеп, түшүндүрмө жазыңыз.")
PromptForChatGPTForKyrgyzAnalogyQuestionEnd = ("Тапшырма: Бул жуптун эмнеге туура экени тууралуу түшүндүрмө бериңиз. "
                                               "Мугалимдин стилинде кыргыз тилинде жазылган, кененирээк түшүндүрмө "
                                               "бериңиз.")
PromptForChatGPTForRussianAnalogyQuestion = ("Ниже даны пары слов, связанные аналогией. В вопросе первая пара слов имеет "
                                             "определённое отношение, которое должно повторяться в одной из предложенных "
                                             "пар в ответах. Проанализируйте вопрос и ответы, и напишите объяснение "
                                             "выбора правильного ответа.")
PromptForChatGPTForRussianAnalogyQuestionEnd = ("Объясните, почему эта пара является правильным вариантом. "
                                                "Напишите развёрнутое объяснение на русском языке в стиле учителя.")
PromptForChatGPTForKyrgyzGrammarQuestion = ("Төмөндө кыргыз тилинин грамматикасы боюнча суроо берилген. "
                                            "Суроону толук анализде.")
PromptForChatGPTForKyrgyzGrammarQuestionEnd = ("Эмнеге бул вариант туура экенин түшүндүрүп бериңиз. Түшүндүрмөнү кыргыз "
                                               "тили мугалиминин стилинде, так жана кененирээк кылып бериңиз. "
                                               "Грамматикалык жана лексикалык аспектилерди белгилеңиз, жоопту талдап "
                                               "түшүндүрүп бериңиз.")
PromptForChatGPTForRussianGrammarQuestion = ("Внизу приведён вопрос по грамматике русского языка. "
                                             "Проведите полный анализ вопроса.")
PromptForChatGPTForRussianGrammarQuestionEnd = ("Объясните, почему этот вариант является правильным. Напишите объяснение "
                                                "в стиле учителя русского языка, чётко и подробно. Укажите "
                                                "грамматические и лексические аспекты, проанализируйте и объясните "
                                                "выбранный ответ.")