import asyncio
import edge_tts

TEXT = "क्या आप जानते हैं? शहद सही से रखा जाए तो लगभग कभी खराब नहीं होता। मिस्र के पुराने मकबरों में हज़ारों साल पुराना शहद मिला है।"

async def main():
    tts = edge_tts.Communicate(TEXT, "hi-IN-MadhurNeural", rate="-5%", pitch="-10Hz")
    await tts.save("voice.mp3")

asyncio.run(main())
