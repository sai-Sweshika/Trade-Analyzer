from fastapi import APIRouter, Depends
from app.utils.auth import verify_token

router = APIRouter()

@router.get("/analyze/{sector}")
async def analyze_sector(sector: str, auth=Depends(verify_token)):
    
    report = f"""
Trade Opportunities Report - {sector.upper()} Sector (India)

* Market Overview:
The {sector} sector is growing rapidly with strong demand.

* Key Trends:
- Increasing investments
- Government support
- Export opportunities

* Trade Opportunities:
- New startups emerging
- High demand in global markets
- Strong supply chain growth

* Risks:
- Market competition
- Regulatory changes

* Conclusion:
The {sector} sector offers strong trade potential in India.
"""

    return {"report": report}