from django.core.mail import send_mail
from admin.settings import EMAIL_HOST_USER


class EMail():

    def setTo(Self, pTo):
        Self.pTo = pTo

    def setNumber(Self, pRFCNumber):
        Self.pRFCNumber = pRFCNumber

    def setTypeComplice(Self, pType):
        if(pType == 1):
            Self.pSub = "Not Complice RFC Number "+Self.pRFCNumber+"."
            Self.pMsg = "You are recive this email because RFC Number " + \
                Self.pRFCNumber+" should are closed."
        elif(pType == 2):
            Self.pSub = "Not Complice RFC Number "+Self.pRFCNumber+"."
            Self.pMsg = "You are recive this email because RFC Number " + \
                Self.pRFCNumber+" should are closed."

    def sendMail(Self, pDest):
        send_mail(Self.pSub, Self.pMsg, EMAIL_HOST_USER,
                  list(pDest), fail_silently=False)
