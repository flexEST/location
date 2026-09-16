from http.server import BaseHTTPRequestHandler
from twilio.rest import Client
import json

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Your Twilio Credentials
        account_sid = "AC0eb95f311e1764627245d71f653de943"
        auth_token = "923525e309031c27c4e184927e23f7fa"
        
        try:
            client = Client(account_sid, auth_token)

            # The alert message in Azerbaijani
            say_message = "Salam! Sizin server tapşırığınız uğurla başa çatdı. Gecəniz xeyrə qalsın."
            twiml_response = f'<Response><Say language="az-AZ">{say_message}</Say></Response>'

            # Place the automated call
            call = client.calls.create(
                to="+994708635805",
                from_="+18573846402",
                twiml=twiml_response,
            )

            # Send success response with CORS headers
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response_data = {"success": True, "sid": call.sid}
            self.wfile.write(json.dumps(response_data).encode('utf-8'))
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({"success": False, "error": str(e)}).encode('utf-8'))

    def do_OPTIONS(self):
        # Handle preflight CORS requests
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
