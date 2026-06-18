# === Stage 35: Add active user switching and user-specific records ===
# Project: CraftFlow
class UserSession:
    def __init__(self, user_id):
        self.user = user_id
        self.records = []
    
    def load(self, filename):
        try:
            with open(filename) as f:
                for line in f:
                    parts = line.strip().split('|')
                    if len(parts) >= 4 and parts[0] == self.user:
                        self.records.append({
                            'material': parts[1],
                            'milestone': parts[2],
                            'cost': float(parts[3]) if parts[3].isdigit() else 0,
                            'note': parts[4]
                        })
        except FileNotFoundError:
            pass
    
    def add_record(self, material, milestone, cost=0.0, note=""):
        self.records.append({
            'material': material,
            'milestone': milestone,
            'cost': float(cost) if isinstance(cost, str) else cost,
            'note': note
        })
    
    def save(self, filename):
        with open(filename, 'w') as f:
            for r in self.records:
                line = '|'.join([self.user, r['material'], r['milestone'], 
                                 str(r['cost']), r['note']])
                f.write(line + '\n')

def get_active_user():
    import os
    user_file = '.craftflow_user'
    if not os.path.exists(user_file):
        return 'guest'
    with open(user_file) as f:
        return f.read().strip()
