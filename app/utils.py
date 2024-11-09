from aiogram import Router

router = Router()

# Dictionary for storing message IDs
sent_message_add_screen_ids = {
    'bot_messages': [],
    'user_messages': []
}

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

PhoneNumberAdmin = '+996702160703'