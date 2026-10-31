# Lab 5 — Static Code Analysis Issue Log

> Line numbers can change after edits. Record the exact line numbers and messages from your own baseline Pylint, Bandit, and Flake8 runs before submitting. The execution environment used to prepare this draft could not install those tools because network access was unavailable, so no tool output is fabricated here.

| Issue | Type / severity | Original location | Description | Fix approach |
|---|---|---:|---|---|
| Unsafe YAML loader | Security / high | `loadConfig`, `yaml.load` | The generic YAML loader can construct Python objects from untrusted YAML. | Replaced with `yaml.safe_load` and basic configuration validation. |
| Hardcoded database password | Security / medium | `connectWardenDb` | A credential is embedded in source and may be exposed in version control. | Read connection settings from environment variables; do not return the password. |
| Debug server enabled | Security / medium | `runPortal` | Debug mode can expose diagnostic information and should not be enabled for normal execution. | Set `debug=False` and bind the development server to localhost. |
| Mutable default argument | Correctness / medium | `allocateRoom(..., preferred=[])` | The default list is shared across calls. | Use `preferred=None` and create a new list inside the function. |
| Incorrect capacity condition | Correctness | `allocateRoom` | `>` allows a room already at capacity to accept another occupant. | Skip a room when occupant count is greater than or equal to capacity. |
| Gender not checked | Correctness | `allocateRoom` | The allocation function can place a student in a block with a different configured gender. | Require the room's configured gender to match the student's gender. |
| Duplicate allocation | Correctness | `allocateRoom` | Repeated calls for one student can add duplicate occupants or overwrite allocation records. | Return the existing room when the student is already allocated. |
| Vacating leaves stale occupant | Correctness | `vacateRoom` | The allocation dictionary is cleared, but the room's occupant list remains unchanged. | Remove the student from both the allocation record and room occupant list. |
| Vacant bed count undercounts | Correctness | `vacantBeds` | It counts capacity only for entirely empty rooms, omitting unoccupied beds in partially occupied rooms. | Sum capacity minus occupant count for every room. |
| Priority ordering inconsistent with label | Correctness | `priorityOrder` | Sorting years in ascending order places junior students before seniors. | Sort in descending order so higher year numbers come first. |
| Unescaped user input in HTML | Security | `roomLookup` | The query parameter is concatenated into HTML, allowing HTML/script injection. | Escape the student identifier and rendered allocation. |
| Unused imports and naming/style | Style | Imports and function names | Unused imports, camelCase names, spacing, and long lines reduce readability and can trigger lint findings. | Remove unused imports, use snake_case, and format consistently. |
| Remote logging configuration listener | Security review | `startRemoteLogConfig` | A remote logging configuration listener can be risky if exposed or invoked without appropriate controls. | Keep it out of startup flow and call it only deliberately; review whether it is needed. |

## Verification checklist

- [ ] Save baseline reports for Pylint, Bandit, and Flake8.
- [ ] Confirm the original findings and exact line numbers from those reports.
- [ ] Run the same three tools on the corrected file and save after reports.
- [ ] Confirm Bandit findings are resolved or document any remaining justified finding.
- [ ] Confirm Flake8 has no output.
- [ ] Confirm Pylint score is above 9.5/10, or document remaining warnings.
- [ ] Run the program and test allocation, duplicate allocation, capacity, gender compatibility, vacancy, fees, and waitlist behavior.
