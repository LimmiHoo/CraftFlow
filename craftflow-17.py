# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: CraftFlow
class DryRunMixin:
    def __init__(self, dry_run=False):
        self._dry_run = dry_run

    @property
    def is_dry_run(self):
        return self._dry_run

    def _execute_action(self, action_func, *args, **kwargs):
        if self.is_dry_run:
            print(f"[DRY-RUN] Would execute: {action_func.__name__} with args={args}, kwargs={kwargs}")
            return None
        else:
            return action_func(*args, **kwargs)

    def add_material(self, name, quantity, cost):
        self._execute_action(lambda n, q, c: print(f"Adding material {n}: {q} units @ ${c:.2f}"), name, quantity, cost)

    def set_milestone(self, title, status, date=None):
        self._execute_action(lambda t, s, d=now(): print(f"Milestone '{t}' is now '{s}' (date: {d})"), title, status, date)

    def log_inspiration(self, source, note):
        self._execute_action(lambda s, n: print(f"Logged inspiration from '{s}': {n}"), source, note)
