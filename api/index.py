from http.server import BaseHTTPRequestHandler
from twilio.rest import Client
import json
import os

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', 'https://app.telebeplus.com')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

        # Print debug info to Vercel function logs
        account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
        auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
        
        print(f"DEBUG SID length: {len(str(account_sid)) if account_sid else 'MISSING'}")
        print(f"DEBUG TOKEN length: {len(str(auth_token)) if auth_token else 'MISSING'}")

        try:
            client = Client(account_sid, auth_token)

            say_message = "Salam! Sizin server tapşırığınız uğurla başa çatdı. Gecəniz xeyrə qalmasın."
            twiml_response = f'<Response><Say language="az-AZ">{say_message}</Say></Response>'

            call = client.calls.create(
                to="+994708635805",
                from_="+18573846402",
                twiml=twiml_response,
            )

            response_data = {"success": True, "sid": call.sid}
            self.wfile.write(json.dumps(response_data).encode('utf-8'))
            
        except Exception as e:
            error_data = {"success": False, "error": str(e)}
            self.wfile.write(json.dumps(error_data).encode('utf-8'))

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', 'https://app.telebeplus.com')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
