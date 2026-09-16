from http.server import BaseHTTPRequestHandler
from twilio.rest import Client
import json

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Set CORS headers first so the browser allows the response
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', 'https://app.telebeplus.com')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

        try:
            # Your exact working credentials and logic
            account_sid = "AC0eb95f311e1764627245d71f653de943"
            auth_token = "923525e309031c27c4e184927e23f7fa"

            client = Client(account_sid, auth_token)

            say_message = "Salam! Sizin server tapşırığınız uğurla başa çatdı. Gecəniz xeyrə qalsın."
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
