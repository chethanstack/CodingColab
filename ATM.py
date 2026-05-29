# 💼 Real-World Problem: ATM Machine Simulator
# 🏦 Problem:
# Build a simple ATM interface using a while loop:
# User has a balance of ₹10,000
# Show a menu:
# Check balance
# Deposit
# Withdraw
# Exit
# Keep running until the user selects Exit
# If withdrawal > balance, show error
import time
pin="0000"
print("🙏Welcome🙏")
print("please insert your card 💳")
time.sleep(3)
count=3
while count>0:
    user_pin = input("Please enter your 4 digit pin:")
    if pin==user_pin:
        balance=10000
        print("please select your language:")
        print("1.English\n2.Telugu\n3.Hindi")
        option=int(input("My option is :"))
        match option:
            case 1:
                print("Select any one option do you want:")
                print("1.check balance\n2.Deposit\n3.Withdraw\n4.Exit")
                sub_option=int(input("Enter the any number of above service you want:"))
                match sub_option:
                    case 1:
                        print(f"Current Balance is : {balance}")
                        break
                    case 2:
                        deposit_amo=int(input("Enter the amount want do deposit:"))
                        if 1<=deposit_amo<=49900:
                            time.sleep(2)
                            balance=balance+deposit_amo
                            print(f"You depositd Rs.{deposit_amo}")
                            final = input("Do you want to see your balance(YES/NO):")
                            if final.lower() == 'yes':
                                print(f"your balance is : {balance}")
                            break
                        else:
                            print('You exceeded toaday limited!!!')
                            break
                    case 3:
                        withdraw=int(input("Enter the amount in terms of X100:"))
                        if withdraw<balance:
                            print("Your transaction is in process:")
                            time.sleep(3)
                            print("Your transaction completed successfully!!")
                            balance=balance-withdraw
                            final=input("Do you want to see your balance(YES/NO):")
                            if final.lower()=='yes':
                                print(f"your balance is : {balance}")
                            break
                        else:
                            print("You dont have Sufficient amount!!")
                            break
                    case 4:
                        print("Thank You! 🙏Visit Again!!🙏")
                        break
                    case _:
                        print("Invalid Option!!")
                        break
            case 2:

                balance = 10000  # ప్రారంభ బ్యాలెన్స్ (ఉదాహరణ కోసం)

                print("దయచేసి మీరు కోరుకునే ఆప్షన్‌ను ఎంచుకోండి:")
                print("1. బ్యాలెన్స్‌ను చూడండి\n2. డిపాజిట్ చేయండి\n3. విత్‌డ్రా చేయండి\n4. బయటకు వెళ్లండి")
                sub_option = int(input("పై సేవలలో మీరు కోరుకునే సంఖ్యను నమోదు చేయండి: "))

                match sub_option:
                    case 1:
                        print(f"ప్రస్తుత బ్యాలెన్స్: ₹{balance}")
                        break

                    case 2:
                        deposit_amo = int(input("డిపాజిట్ చేయదలచిన మొత్తాన్ని నమోదు చేయండి: "))
                        if 1 <= deposit_amo <= 49900:
                            time.sleep(2)
                            balance = balance + deposit_amo
                            print(f"మీరు ₹{deposit_amo} డిపాజిట్ చేశారు.")
                            final = input("మీ బ్యాలెన్స్‌ను చూడాలా? (YES/NO): ")
                            if final.lower() == 'yes':
                                print(f"మీ ప్రస్తుత బ్యాలెన్స్: ₹{balance}")
                            break
                        else:
                            print("మీరు ఈ రోజు పరిమితిని మించిపోయారు!!!")
                            break

                    case 3:
                        withdraw = int(input("దయచేసి ₹100ల పదంలో విత్‌డ్రా చేయదలచిన మొత్తాన్ని నమోదు చేయండి: "))
                        if withdraw < balance:
                            print("మీ లావాదేవీ ప్రక్రియలో ఉంది...")
                            time.sleep(3)
                            print("మీ లావాదేవీ విజయవంతంగా పూర్తయింది!!")
                            balance = balance - withdraw
                            final = input("మీ బ్యాలెన్స్‌ను చూడాలా? (YES/NO): ")
                            if final.lower() == 'yes':
                                print(f"మీ ప్రస్తుత బ్యాలెన్స్: ₹{balance}")
                            break
                        else:
                            print("మీకు తగినంత మొత్తము లేదు!!")
                            break

                    case 4:
                        print("ధన్యవాదాలు! 🙏 మళ్ళీ కలుద్దాం!! 🙏")
                        break

                    case _:
                        print("చెల్లని ఎంపిక!!")
                        break
            case 3:


                print("कृपया नीचे दिए गए विकल्पों में से कोई एक चुनें:")
                print("1. बैलेंस देखें\n2. जमा करें\n3. निकासी करें\n4. बाहर निकलें")
                sub_option = int(input("आप जिस सेवा का उपयोग करना चाहते हैं उसका नंबर दर्ज करें: "))

                match sub_option:
                    case 1:
                        print(f"आपका वर्तमान बैलेंस है: ₹{balance}")
                        break

                    case 2:
                        deposit_amo = int(input("आप जितनी राशि जमा करना चाहते हैं उसे दर्ज करें: "))
                        if 1 <= deposit_amo <= 49900:
                            time.sleep(2)
                            balance = balance + deposit_amo
                            print(f"आपने ₹{deposit_amo} जमा किए हैं।")
                            final = input("क्या आप अपना बैलेंस देखना चाहते हैं? (YES/NO): ")
                            if final.lower() == 'yes':
                                print(f"आपका वर्तमान बैलेंस है: ₹{balance}")
                            break
                        else:
                            print("आपने आज की लिमिट पार कर दी है!!!")
                            break

                    case 3:
                        withdraw = int(input("₹100 के गुणक में निकासी राशि दर्ज करें: "))
                        if withdraw < balance:
                            print("आपका ट्रांज़ैक्शन प्रक्रिया में है...")
                            time.sleep(3)
                            print("आपका ट्रांज़ैक्शन सफलतापूर्वक पूरा हो गया है!!")
                            balance = balance - withdraw
                            final = input("क्या आप अपना बैलेंस देखना चाहते हैं? (YES/NO): ")
                            if final.lower() == 'yes':
                                print(f"आपका वर्तमान बैलेंस है: ₹{balance}")
                            break
                        else:
                            print("आपके पास पर्याप्त राशि नहीं है!!")
                            break

                    case 4:
                        print("धन्यवाद! 🙏 फिर से आइए!! 🙏")
                        break

                    case _:
                         print("अमान्य विकल्प!!")
                         break

            case _:
                print("Invalid  language option! Try again")
                break

    else:
        print("You entered wrong pin❌\nplease enter right pin.....")
        count-=1
        print(f"Still you have remaining {count} chances")
if count==0:
    print("You had Reached your ATM Usage limit")
    print("_"*45)
    print("Try Tomorrow☹️....")

