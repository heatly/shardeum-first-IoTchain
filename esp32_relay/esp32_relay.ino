#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "oppo";
const char* password = "12345678";
const char* api_url = "https://api-unstable.shardeum.org";

void setup() {
    Serial.begin(115200);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    Serial.println("Connected to WiFi");
}

void loop() {
    HTTPClient http;
    http.begin(api_url);
    int httpCode = http.GET();
    if (httpCode > 0) {
        String payload = http.getString();
        Serial.println(payload);
    }
    http.end();
    delay(10000);
}
