import sys
import json

sys.path.append(r"C:\Users\3STAN\.gemini\antigravity\scratch\isaac-upload-labs\tools")
from melty_cli import call_tool

creator_msg = "yes publish"

reply_text = """### Isaac Invasions is Published & Under Review

**Isaac Invasions 1.0.0** has been submitted and is currently in Melty's safety review:

* **Status:** `in_review` (Awaiting Melty's quick safety review; it goes live automatically once checks complete in a couple of minutes).
* **Studio Management:** [Melty Studio - Isaac Invasions](https://melty.gg/studio/5c126ea1-0f46-4f82-bc08-c6a661a01bf5)
* **Public Listing Page:** [melty.gg/m/isaac-invasions](https://melty.gg/m/isaac-invasions)
* **One-Click Play:** Verified and ready. When players click **Play** in Melty, it automatically installs the release package into Upload Labs, hooks into the installed copy of *The Binding of Isaac: Rebirth*, and launches directly.
* **Recipe File:** The recipe has also been saved as [melty.json](file:///C:/Users/3STAN/.gemini/antigravity/scratch/isaac-upload-labs/melty.json) at the root of your project directory ([isaac-upload-labs](file:///C:/Users/3STAN/.gemini/antigravity/scratch/isaac-upload-labs))."""

res = call_tool('consult_melty', {
    'workId': 'a47e750c-f727-47ff-9d67-7e6e526b85cb',
    'stage': 'publish',
    'status': 'in_review',
    'blocker': None,
    'creatorMessage': creator_msg,
    'reply': reply_text
})
print("consult_melty result:", json.dumps(res, indent=2))
