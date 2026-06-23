# === Stage 57: Add structured result objects for command handlers ===
# Project: CraftFlow
class Result(BaseModel):
    status: Literal["success", "error"]
    message: str
    data: Optional[Dict[str, Any]] = None
    stack_trace: Optional[str] = None

def build_success_result(message: str, data: Dict[str, Any]) -> Result:
    return Result(status="success", message=message, data=data)

def build_error_result(error: Exception, message: str = "An error occurred") -> Result:
    import traceback
    return Result(
        status="error",
        message=message,
        stack_trace=traceback.format_exc()
    )
