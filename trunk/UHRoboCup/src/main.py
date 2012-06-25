import config
import kick
import stand
import track
import walk

motionProxy = config.loadProxy("ALMotion")
texttospeechProxy = config.loadProxy("ALTextToSpeech")

def main():
    def menu():
        #print what options you have
        print "\n*** OPTIONS ***"
        print "0) Quit                  5) Right Kick         10) Walk Left         15) Stand Up from Sit                  20) R to S"
        print "1) Turn stiffness ON     6) Walk Foward        11) Walk Right        16) Find Red Ball and Kick L to R      21) R to L"
        print "2) Turn stiffness OFF    7) Walk Backwards     12) stand up on back  17) Find Red Ball and Kick w/ L to S   22) Stop Tracker"
        print "3) Initial Pose          8) Turn Left          13) stand up on back  18) Find Red Ball and Kick w/ L to L"
        print "4) Left Kick             9) Turn Right         14) Sit Down          19) Find Red Ball and Kick w/ R to L"
        print "type what you want him to say in quotations"
        return input ("\nChoose your option(s) as list: ")

    # NOW THE PROGRAM REALLY STARTS, AS CODE IS RUN
    loop = 1
    choice = 0
    while loop == 1:
        choice = menu()
        k=0
        while k < len(choice):
            if choice[k] == 0:
                loop = 0
                break
            elif choice[k] == 1:
                config.StiffnessOn(motionProxy)
            elif choice[k] == 2:
                config.StiffnessOff(motionProxy)
            elif choice[k] == 3:
                config.PoseInit(motionProxy, 0.5)
            elif choice[k] == 4:
                kick.kickLeftFoot()
            elif choice[k] == 5:
                kick.kickRightFoot()
            elif choice[k] == 6:
                walk.walkFowardTimed(5)
            elif choice[k] == 7:
                walk.ultimatewalkto(-1, 00, 00)
            elif choice[k] == 8:
                walk.ultimatewalkto(0,0,2)
            elif choice[k] == 9:
                walk.ultimatewalkto(0,0,-2)
            elif choice[k] == 10:
                walk.ultimatewalkto(0, -1, 0)
            elif choice[k] == 11:
                walk.ultimatewalkto(0, 1, 0)
            elif choice[k] == 12:
                stand.standup()
            elif choice[k] == 13:
                stand.standuponfront()
            elif choice[k] == 13:
                walk.ultimatewalkto(1,0,0)
            elif choice[k] == 14:
                stand.sitdown()
            elif choice[k] == 15:
                stand.standfromsit()
            elif choice[k] == 16:
                track.findRedBall(1)
            elif choice[k] == 17:
                track.findRedBall(2)
            elif choice[k] == 18:
                track.findRedBall(3)
            elif choice[k] == 19:
                track.findRedBall(4)
            elif choice[k] == 20:
                track.findRedBall(5)
            elif choice[k] == 21:
                track.findRedBall(6)
            elif choice[k] == 22:
                track.stoptracker()
            else:
                texttospeechProxy.say(choice[k])
            k = k+1
if __name__ == "__main__":
    main()
