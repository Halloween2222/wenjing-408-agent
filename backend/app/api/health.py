"""服务自检接口。

非契约接口，仅用于部署健康检查与联调排查（题库是否加载、多少题、多少已核验）。
不参与 Apifox 契约，若 TL 认为不需要可直接删除本文件与 main.py 中的注册。
"""

from __future__ import annotations

from fastapi import APIRouter, Depends

from app.deps import get_question_store, get_retrieval_service
from app.services import text_utils
from app.services.question_store import QuestionStore
from app.services.retrieval import RetrievalService

router = APIRouter(prefix="/api", tags=["ops"])


@router.get("/health")
def health(
    store: QuestionStore = Depends(get_question_store),
    service: RetrievalService = Depends(get_retrieval_service),
) -> dict:
    stats = store.stats()
    return {
        "status": "ok",
        "questions": stats["total"],
        "by_subject": stats["by_subject"],
        "by_review_state": stats["by_review_state"],
        "skipped": stats["skipped"],
        "tokenizer": "jieba" if text_utils.HAS_JIEBA else "fallback-bigram",
        "indexed": service.size,
    }
