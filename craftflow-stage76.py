# === Stage 76: Add graceful keyboard interrupt handling in the CLI entry point ===
# Project: CraftFlow
import signal
from typing import Optional, Callable


def setup_signal_handlers(
    on_interrupt: Optional[Callable[[Optional[str]], None]] = None,
) -> None:
    """Register graceful handlers for SIGINT and SIGTERM."""
    def handler(signum: int, frame: Optional[int]) -> None:
        if signum in (signal.SIGINT, signal.SIGTERM):
            print("\n\n[CraftFlow] Received interrupt signal. Shutting down gracefully...")
            if on_interrupt is not None:
                try:
                    on_interrupt(None)
                except Exception as e:
                    print(f"[CraftFlow] Error during shutdown cleanup: {e}")
            else:
                # Default exit without specific cleanup logic defined by user yet
                pass
            raise SystemExit(0)

    signal.signal(signal.SIGINT, handler)
    signal.signal(signal.SIGTERM, handler)
