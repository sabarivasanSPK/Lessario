import re

# Shot number → Tamil+English dialogue
dialogues = {
    4:   "இது கொஞ்சம் thrill ஆ இருக்கு… ஆனா செம்ம fun ஆவும் இருக்கு!",
    13:  "Sssaarapaambu… நீயா அது?",
    14:  "நான் இங்க இருக்கேன்",
    16:  "ஆத்தாடி… வேஷத்த கொத்தி கித்தி வேச்சுராத…",
    24:  "ஐயோ! என்ன அது?!",
    35:  "ஏதும் காத்து கருப்பா இருக்குமோ?",
    37:  "காத்தும் கிடையாது கருப்பும் கிடையாது… யாரோ ரொம்ப speed ஆ போறாங்க…",
    39:  "அது யாரு என்னவிட speed ஆ… இந்த காட்டுலயே நான்தான் speed ஆன மிருகம்…",
    42:  "ஆதாவது… நான்தான் Rajavukku அடுத்து ரெண்டாவது speed ஆன மிருகம்",
    44:  "முயலவிட speed ஆன மிருகம் நெறிய இருக்கு Muttagose… குதிரை, வேங்கை, மான்",
    45:  "ஆமா… வேங்கை, சுரா, சிங்கம், அதான் நம்ம Raja… Animals பெருக்கு பதிலா cinema படத்தோட பேரா சொல்லிட்டு இருக்கீங்க அக்கா…",
    51:  "My dear மிருகங்களே, பறவைகளே, பூச்சிகளே… நம்ம காட்டுக்குள்ள நமக்கு பழக்கம் இல்லாத ஒருத்தர் வந்திருக்காங்க… அவங்க யாருன்னு கண்டுபிடிக்க வேண்டிய நேரம் வந்துருச்சு…",
    71:  "Raja… அங்க யாரோ அசையுர மாதிரி இருந்துச்சு",
    75:  "Raja… அவங்கள விடாதீங்க… நீங்க ஓங்கி அடிச்சா ஒண்ட்ரா ton weight-uh னு அவங்களுக்கு காட்டுங்க…",
    93:  "யாரோ நம்ம காட்ட தாக்க வராங்க போல…",
    94:  "இது attack இல்ல… இது control இல்லாத movement.",
    95:  "சிங்கம் மட்டும் இல்லாம வேற சில பூனை வகை மிருகங்களுக்கும் இதே மாதிரி கால் தடம் இருக்கும் Muttagose…",
    101: "யார் நீ… உனக்கு என்ன வேணும்",
    104: "நான் பயணிக்க எனக்கு ஒரு வழி வேணும்… அத நான் எடுத்துக்குரேன்…",
    107: "நீ இப்படி போனா… காடு மொத்தமும் அழிஞ்சிரும்…",
    108: "வேகமா ஓடுனா தான் என்னால உயிர் வாழ முடியும்.",
    182: "இவ்வளோ பலம் இருந்தா அத கட்டுப்படுத்த முயற்சி பண்ணு… எப்போ நீ உன் பலத்த உன் control ல வேச்சுருக்கியோ அப்போ இந்த உலகத்துல ஏத வேணும்னாலும் உன் control ல வைக்கலாம்",
    187: "இப்போ என்ன கவனிச்சு பாரு",
    204: "வேகம் மட்டும் தான் என்னோட பலம்னு நினைச்சேன்… ஆனா உண்மையான பலம்னா என்னன்னு புரிய வேச்சுட்டீங்க Raja",
    207: "அண்ணா… நீங்க Singu Rajavukku shave பண்ணி tattoo போட மாதிரி இருக்கீங்க… உங்க பேரு என்ன?",
    208: "பேரா… எனக்கு யாரும் இன்னும் பேரு வைக்கல.",
    209: "பேரு இல்லன என்ன. நீ இனிமே எனக்கு தம்பி மாதிரி.",
    211: "என் பேரு Thambi… நான் ஒரு புலி…",
    214: "Singuve easy ஆன எதிரி இல்ல… இப்போ Singuvukku ஒரு தம்பி வேரயா… பாத்துக்கலாம்…",
    220: "Fast வேண்டாம்… நமக்கு slow தான் better!",
}

input_path  = "E7_Shot_Prompts.md"
output_path = "E7_Shot_Prompts.md"

with open(input_path, encoding="utf-8") as f:
    lines = f.readlines()

out = []
for line in lines:
    stripped = line.rstrip("\n")

    # --- Table header row ---
    if re.match(r"\| Shot # \| Characters \|", stripped):
        stripped = stripped.rstrip(" |") + " | Dialogue (Tamil+English) |"
        out.append(stripped + "\n")
        continue

    # --- Table separator row ---
    if re.match(r"\|[-]+\|[-]+\|", stripped):
        stripped = stripped.rstrip(" |") + "|:---|"
        out.append(stripped + "\n")
        continue

    # --- Shot data row ---
    m = re.match(r"\| (\d+) \|", stripped)
    if m:
        shot_num = int(m.group(1))
        dialogue = dialogues.get(shot_num, "—")
        stripped = stripped.rstrip(" |") + f" | {dialogue} |"
        out.append(stripped + "\n")
        continue

    out.append(line)

with open(output_path, "w", encoding="utf-8") as f:
    f.writelines(out)

print("Done! Dialogue column added to all", len(dialogues), "dialogue shots.")
