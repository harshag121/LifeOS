from fastapi import APIRouter

router = APIRouter()

@router.get("/boosters")
async def boosters():
    return {
        "tools": ["neural_mindmaps", "concept_fusion"],
        "creativity_boosters": [
            "constraint_generation",
            "cross_domain_prompting"
        ]
    }
